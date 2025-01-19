from aiokafka import AIOKafkaProducer
from .config import settings
import asyncio
import json


async def init_kafka():
    kafka_applications_producer = AIOKafkaProducer(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVER,
        value_serializer=lambda x: json.dumps(x).encode()
    )
    await kafka_applications_producer.start()
    return kafka_applications_producer

async def stop_kafka(producer: AIOKafkaProducer):
    if producer is not None:
        await producer.stop()