from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    KAFKA_SERVER: str
    KAFKA_TOPIC: str

    class Config:
        env_file = ".env"


settings = Settings()