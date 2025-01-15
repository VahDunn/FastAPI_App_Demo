from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncAttrs
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings
from ..db.models.base import Base

DATABASE_URL = settings.DATABASE_URL
engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)
async_session: sessionmaker = sessionmaker(# type: ignore
    engine, expire_on_commit=False, class_=AsyncSession) # type: ignore

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)