from aiokafka import AIOKafkaProducer
from .config import settings

kafka_applications_producer: AIOKafkaProducer | None = None

async def init_kafka():
    global kafka_applications_producer
    kafka_applications_producer = AIOKafkaProducer(bootstrap_servers=settings.KAFKA_SERVER)
    await kafka_applications_producer.start()

async def stop_kafka():
    if kafka_applications_producer is not None:
        await kafka_applications_producer.stop()