#!/bin/bash

# Pull the Docker image (for 16GB Ram machines)
docker pull stephanederrode/docker-cluster-hadoop-spark-python-16:3.5

# Create a network called 'hadoop'
docker network create hadoop

# Launch the hadoop cluster containers
docker run --platform linux/amd64 -itd --net=hadoop \
  -p 9870:9870 -p 8088:8088 -p 7077:7077 -p 16010:16010 -p 9999:9999 \
  --name hadoop-master --hostname hadoop-master \
  stephanederrode/docker-cluster-hadoop-spark-python-16:3.5

# Launch the first slave container
docker run --platform linux/amd64 -itd -p 8040:8042 --net=hadoop \
  --name hadoop-slave1 --hostname hadoop-slave1 \
  stephanederrode/docker-cluster-hadoop-spark-python-16:3.5

# Launch the second slave container
docker run --platform linux/amd64 -itd -p 8041:8042 --net=hadoop \
  --name hadoop-slave2 --hostname hadoop-slave2 \
  stephanederrode/docker-cluster-hadoop-spark-python-16:3.5

# Start the docker-compose services
docker-compose up -d

# Create the folder tree
docker exec hadoop-master mkdir -p /opt/spark/jars
docker exec hadoop-master mkdir -p /root/sales

# Copy JDBC driver to the master container
docker cp postgresql-42.7.3.jar hadoop-master:/opt/spark/jars/

# Copy the sales files to the master container
docker cp bike_Sales_analysis/Sales_extract100.csv hadoop-master:/root/sales

# Copy the scripts to the master container
docker cp bike_sales_analysis/batch/revenue_per_category/revenue_per_category.py hadoop-master:/root/sales

# Set JAVA_HOME based on the architecture (AMD or ARM)

# Check if the platform is ARM (specific for recent Apple systems with ARM processors)
if [[ "$(uname -m)" == "arm64" || "$(uname -m)" == "aarch64" ]]; then
  # Set JAVA_HOME for ARM architecture
  docker exec hadoop-master bash -c 'echo export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-arm64" >> /root/.bashrc'
  docker exec hadoop-master bash -c 'source /root/.bashrc'

  # Edit hadoop-env.sh for ARM
  docker exec hadoop-master bash -c 'sed -i "s|export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64|export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64|g" /usr/local/hadoop/etc/hadoop/hadoop-env.sh'
  echo "Config for ARM architecture done"
else
  # Set JAVA_HOME for AMD architecture
  docker exec hadoop-master bash -c 'echo export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64" >> /root/.bashrc'
  docker exec hadoop-master bash -c 'source /root/.bashrc'
  echo "Config for AMD architecture done"
fi
