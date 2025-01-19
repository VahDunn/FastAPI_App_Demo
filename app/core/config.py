from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    KAFKA_BOOTSTRAP_SERVER: str
    KAFKA_TOPIC: str

    model_config = SettingsConfigDict(env_file="app/core/settings.env")


settings = Settings()