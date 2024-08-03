from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

# Define schema for the data
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

# Create Spark session
spark = SparkSession \
    .builder \
    .appName("KafkaSparkStreaming") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.3.6") \
    .getOrCreate()

# Read from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "real_time_data") \
    .load()

# Convert value column to string
df = df.selectExpr("CAST(value AS STRING)")

# Parse JSON data
df_parsed = df.select(from_json(col("value"), schema).alias("data")).select("data.*")

# Write stream to PostgreSQL
query = df_parsed.writeStream \
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
