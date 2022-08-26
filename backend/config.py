from functools import lru_cache
from tortoise import Tortoise
from pydantic import BaseSettings
from decouple import config


class Settings(BaseSettings):
    POSTGRES_DB: str = config("POSTGRES_DB")
    POSTGRES_USER: str = config("POSTGRES_USER")
    POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD")

    DB_HOST: str = config("DB_HOST")
    DB_PORT: int = config("DB_PORT")


@lru_cache()
def get_settings() -> Settings:
    return Settings()


async def init_db():
    settings = get_settings()
    DB_URL = "postgres://{}:{}@{}:{}/{}".format(
        settings.POSTGRES_USER,
        settings.POSTGRES_PASSWORD,
        settings.DB_HOST,
        settings.DB_PORT,
        settings.POSTGRES_DB,
    )
    await Tortoise.init(db_url=DB_URL, modules={"models": ["models"]})
    await Tortoise.generate_schemas()
