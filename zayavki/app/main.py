from .api.endpoints.applications import application_router
from .core.database import init_db, stop_db
from .core.kafka import init_kafka, stop_kafka

from fastapi import FastAPI


app = FastAPI(
    title ="Application Service",
    description = "Сервис для обработки заявок пользователей",
    version = "1.0.0"
)

@app.on_event("startup")
async def startup_event():
    await init_db()
    await init_kafka()


@app.on_event("shutdown")
async def shutdown_event():
    await stop_kafka()
    await stop_db()


@app.get("/")
def hello():
    return {"message": "Выглядишь солидно :)"}


app.include_router(application_router, prefix='/applications', tags=['Applications'])

