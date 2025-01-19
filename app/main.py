from .api.endpoints.applications import application_router
from .core.database import init_db, stop_db
from .core.kafka import init_kafka, stop_kafka
from .core.app import app


@app.on_event("startup")
async def startup_event():
    await init_db()
    app.producer = await init_kafka()


@app.on_event("shutdown")
async def shutdown_event():
    await stop_kafka(app.producer)
    await stop_db()


@app.get("/")
def hello():
    return "Привет! Выглядишь отлично."


app.include_router(application_router, prefix='/applications', tags=['Applications'])

