from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    KAFKA_SERVER: str
    KAFKA_TOPIC: str

    class Config:
        env_file = "/Users/vladislavmorozov/Documents/Dev/FastAPI_Zayavochki/app/core/settings.env"


settings = Settings()