from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder \
    .appName("RevenuePerSubCategory") \
    .getOrCreate()

# Read data from HDFS
df = spark.read.csv("hdfs://hadoop-master:9870/input/Sales.csv", header=True, inferSchema=True)

# Calculate total revenue per sub-category
sub_category_revenue = df.groupBy("Sub_Category").sum("Revenue")

# Rename columns for clarity
sub_category_revenue = sub_category_revenue.withColumnRenamed("sum(Revenue)", "total_revenue")

# Print the results for verification
sub_category_revenue.show()

# Define PostgreSQL connection properties
jdbc_url = "jdbc:postgresql://bike_postgres:5432/bike_db"
connection_properties = {
    "user": "postgres",
    "password": "secret",
    "driver": "org.postgresql.Driver"
}

# Write the result to PostgreSQL
sub_category_revenue.write.jdbc(url=jdbc_url, table="sub_category_revenue", mode="append", properties=connection_properties)

# Stop Spark session
spark.stop()
