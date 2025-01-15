from .api.endpoints.applications import application_router
from .core.database import init_db

from fastapi import FastAPI


app = FastAPI(
    title ="Application Service",
    description = "Сервис для обработки заявок пользователей",
    version = "1.0.0"
)

app.include_router(application_router, prefix='/applications', tags=['Applications'])

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/")
def hello():
    return {"message": "Выглядишь солидно :)"}

