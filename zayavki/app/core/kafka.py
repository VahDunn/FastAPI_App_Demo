from aiokafka import AIOKafkaProducer
from .config import settings

producer: AIOKafkaProducer | None = None

async def init_kafka():
    global producer
    producer = AIOKafkaProducer(bootstrap_servers=settings.KAFKA_SERVER)
    await producer.start()

async def stop_kafka():
    if producer is not None:
        await producer.stop()