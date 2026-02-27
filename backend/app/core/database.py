from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

DATABASE_URL: str = (
    "postgresql+asyncpg://analyst_user:analyst_password@postgres:5432/analyst_platform"
)

engine = create_async_engine(DATABASE_URL, echo=False)

SessionFactory = async_sessionmaker(
    engine,
    expire_on_commit=False,
)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionFactory() as session:
        yield session
