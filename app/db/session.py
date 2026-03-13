from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio.engine import create_async_engine
from typing import AsyncGenerator

from app.core.settings import settings


engine = create_async_engine(settings.DB_URL)


async def get_session() -> AsyncGenerator[AsyncSession]:
    global engine
    async with AsyncSession(engine) as session:
        yield session
