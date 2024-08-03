import time
from kafka.errors import NoBrokersAvailable
from kafka import KafkaProducer
import json

def get_kafka_producer():
    max_retries = 5
    for i in range(max_retries):
        try:
            producer = KafkaProducer(
                bootstrap_servers=['kafka:9092'],
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            return producer
        except NoBrokersAvailable:
            print(f"No brokers available, retrying {i+1}/{max_retries}...")
            time.sleep(5)
    raise Exception("Failed to connect to Kafka broker")

producer = get_kafka_producer()
