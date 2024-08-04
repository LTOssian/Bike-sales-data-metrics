from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_date, when
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

schema = StructType([
    StructField("Date", StringType(), True),
    StructField("Day", IntegerType(), True),
    StructField("Month", IntegerType(), True),
    StructField("Year", IntegerType(), True),
    StructField("Customer_Age", IntegerType(), True),
    StructField("Age_Group", StringType(), True),
    StructField("Customer_Gender", StringType(), True),
    StructField("Country", StringType(), True),
    StructField("State", StringType(), True),
    StructField("Product_Category", StringType(), True),
    StructField("Sub_Category", StringType(), True),
    StructField("Product", StringType(), True),
    StructField("Order_Quantity", IntegerType(), True),
    StructField("Unit_Cost", FloatType(), True),
    StructField("Unit_Price", FloatType(), True),
    StructField("Profit", FloatType(), True),
    StructField("Cost", FloatType(), True),
    StructField("Revenue", FloatType(), True)
])

spark = SparkSession.builder \
    .appName("KafkaSparkListener") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka1:19092") \
    .option("subscribe", "real_time_data") \
    .load()


# Convert the value column from bytes to string and parse JSON

df = df.selectExpr("CAST(value AS STRING) as json_value")
df = df.select(from_json(col("json_value"), schema).alias("data")).select("data.*")

# Map input values to match the values in the database
df = df.withColumn("Customer_Gender", 
                   when(col("Customer_Gender") == "Male", "M")
                   .when(col("Customer_Gender") == "Female", "F")
                   .otherwise(col("Customer_Gender")))
df = df.withColumn("Date", to_date(col("Date"), "yyyy-MM-dd"))

# Write stream to PostgreSQL
query = df.writeStream \
    .foreachBatch(lambda batch_df, _: batch_df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://bike_postgres:5432/bike_db") \
        .option("dbtable", "sales_data") \
        .option("user", "postgres") \
        .option("password", "secret") \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()) \
    .outputMode("append") \
    .start()

query.awaitTermination()
