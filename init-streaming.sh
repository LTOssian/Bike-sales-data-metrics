# Start FastAPI server
docker-compose -f docker-compose.stream.yml up -d

# Start Spark Streaming job
docker cp bike_sales_analysis/stream/spark_listener.py hadoop-master:/root/sales
docker exec hadoop-master /bin/bash -c "spark-submit --jars /opt/spark/jars/postgresql-42.7.3.jar --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 /root/sales/spark_listener.py"