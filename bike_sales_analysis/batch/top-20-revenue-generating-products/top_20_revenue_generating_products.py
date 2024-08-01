from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Top20Products") \
    .getOrCreate()

# Read data from HDFS
df = spark.read.csv("hdfs://hadoop-master:9000/input/Sales.csv", header=True, inferSchema=True)

# Print schema to verify columns
df.printSchema()

# Calculate total revenue per product globally (not filtering by country)
product_revenue_global = df.groupBy("Product").sum("Revenue")

# Rename columns for clarity
product_revenue_global = product_revenue_global.withColumnRenamed("sum(Revenue)", "total_revenue")
product_revenue_global = product_revenue_global.withColumnRenamed("Product", "product_name")

# Get the top 20 products by total revenue globally
top_20_products_global = product_revenue_global.orderBy(col("total_revenue").desc()).limit(20)

# Print the results for verification
top_20_products_global.show()

# Define PostgreSQL connection properties
jdbc_url = "jdbc:postgresql://bike_postgres:5432/bike_db"
connection_properties = {
    "user": "postgres",
    "password": "secret",
    "driver": "org.postgresql.Driver"
}

# Write the DataFrame to PostgreSQL
try:
    top_20_products_global.write.jdbc(url=jdbc_url, table="top_20_products_global", mode="append", properties=connection_properties)
    print("Data written successfully to top_20_products_global table.")
except Exception as e:
    print(f"An error occurred: {e}")

# Stop Spark session
spark.stop()
