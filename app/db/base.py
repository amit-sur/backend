from sqlmodel import SQLModel

from app.db.session import engine


async def init_db():
    global engine
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
