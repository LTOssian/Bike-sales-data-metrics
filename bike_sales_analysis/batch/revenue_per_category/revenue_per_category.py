from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("CategoryRevenue") \
    .getOrCreate()

# Read data from HDFS
df = spark.read.csv("hdfs://hadoop-master:9000/input/Sales.csv", header=True, inferSchema=True)

# Print schema to verify columns
df.printSchema()

# Calculate revenue by Product_Category
category_revenue = df.groupBy("Product_Category").sum("Revenue")
category_revenue = category_revenue.withColumnRenamed("sum(Revenue)", "total_revenue")
category_revenue = category_revenue.withColumnRenamed("Product_Category", "category_name")

# Print results
category_revenue.show()

# Define PostgreSQL connection properties
jdbc_url = "jdbc:postgresql://bike_postgres:5432/bike_db"
connection_properties = {
    "user": "postgres",
    "password": "secret",
    "driver": "org.postgresql.Driver"
}

# Write the DataFrame to PostgreSQL
try:
    category_revenue.write.jdbc(url=jdbc_url, table="category_revenue", mode="append", properties=connection_properties)
    print("Data written successfully to category_revenue table.")
except Exception as e:
    print(f"An error occurred: {e}")

# Stop Spark session
spark.stop()
