from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer
from get_kafka_producer import producer
import json

app = FastAPI()

class SaleData(BaseModel):
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

@app.post("/produce/")
async def produce(sale: SaleData):
    producer.send("real_time_data", value=sale.dict())
    return {"status": "Message sent"}
