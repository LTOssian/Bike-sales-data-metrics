from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder \
    .appName("CategoryRevenue") \
    .getOrCreate()

# Read data from HDFS
df = spark.read.csv("hdfs://hadoop-master:9000/input/Sales.csv", header=True, inferSchema=True)

# Print schema to verify columns
df.printSchema()

# Filter for sales in France and calculate total revenue per product
france_sales = df.filter(col("Country") == "France")
product_revenue_france = france_sales.groupBy("Product").sum("Revenue")

# Rename columns for clarity
product_revenue_france = product_revenue_france.withColumnRenamed("sum(Revenue)", "total_revenue")

# Get the top 10 products by total revenue in France
top_10_products_france = product_revenue_france.orderBy(col("total_revenue").desc()).limit(10)

# Define PostgreSQL connection properties
jdbc_url = "jdbc:postgresql://bike_postgres:5432/bike_db"
connection_properties = {
    "user": "postgres",
    "password": "secret",
    "driver": "org.postgresql.Driver"
}

# Write the DataFrame to PostgreSQL
top_10_products_france.write.jdbc(url=jdbc_url, table="top_10_products_france", mode="append", properties=connection_properties)

# Stop Spark session
spark.stop()
