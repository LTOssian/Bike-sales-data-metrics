# Start FastAPI server
docker-compose -f docker-compose.stream.yml up -d

# Start Spark Streaming job
docker exec hadoop-master /bin/bash -c "spark-submit --jars /opt/spark/jars/postgresql-42.7.3.jar /root/sales/spark_listener.py"
