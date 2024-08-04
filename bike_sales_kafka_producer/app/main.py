from fastapi import FastAPI
from kafka import KafkaProducer
from pydantic import BaseModel
import json
import logging
import os

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SalesData(BaseModel):
    Date: str
    Day: int
    Month: int
    Year: int
    Customer_Age: int
    Age_Group: str
    Customer_Gender: str
    Country: str
    State: str
    Product_Category: str
    Sub_Category: str
    Product: str
    Order_Quantity: int
    Unit_Cost: float
    Unit_Price: float
    Profit: float
    Cost: float
    Revenue: float

class KafkaProducerSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        """Static access method."""
        if KafkaProducerSingleton._instance is None:
            KafkaProducerSingleton()
        return KafkaProducerSingleton._instance

    def __init__(self):
        """Virtually private constructor."""
        if KafkaProducerSingleton._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            # Get the Kafka broker URL from environment variables or default to 'localhost:9092'
            kafka_broker = os.getenv("KAFKA_BROKER", "kafka1:19092")
            KafkaProducerSingleton._instance = KafkaProducer(
                bootstrap_servers=[kafka_broker],
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )


# API endpoint to send data to Kafka
@app.post("/produce/")
async def produce(data: SalesData):
    try:
        # Get the Kafka producer instance
        producer = KafkaProducerSingleton.get_instance()

        # Send data to the Kafka topic "real_time_data"
        producer.send("real_time_data", value=data.dict())

        # Log the sent data
        logger.info(f"Message sent: {data.dict()}")

        return {"status": "Message sent"}
    except Exception as e:
        logger.error(f"Error sending message: {str(e)}")
        return {"status": "Failed", "error": str(e)}
