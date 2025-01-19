from fastapi import FastAPI
from ..utils.logger import LOG


app = FastAPI(
    title ="Application Service",
    description = "Сервис для обработки заявок пользователей",
    version = "1.0.0"
)


LOG.info("FastAPI says Hello!")