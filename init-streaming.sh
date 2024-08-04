# Start FastAPI server
docker-compose -f docker-compose.stream.yml up -d
echo "Wait for kafka"
sleep 10

curl --location 'localhost:8000/produce/' \
--header 'Content-Type: application/json' \
--data '{
           "Date": "2024-08-02",
           "Day": 2,
           "Month": 8,
           "Year": 2024,
           "Customer_Age": 18,
           "Age_Group": "Young Adults (25-34)",
           "Customer_Gender": "Male",
           "Country": "Belgium",
           "State": "California",
           "Product_Category": "Bikes",
           "Sub_Category": "Mountain Bikes",
           "Product": "MTB 1000",
           "Order_Quantity": 1,
           "Unit_Cost": 200.00,
           "Unit_Price": 250.00,
           "Profit": 50.00,
           "Cost": 200.00,
           "Revenue": 250.00
         }'
sleep 5

# Start Spark Streaming job
docker cp bike_sales_analysis/stream/spark_listener.py hadoop-master:/root/sales
docker exec hadoop-master /bin/bash -c "spark-submit --jars /opt/spark/jars/postgresql-42.7.3.jar --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 /root/sales/spark_listener.py"