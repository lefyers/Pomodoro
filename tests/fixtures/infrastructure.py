import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from app.Infrastructure.database.database import Base
from app.settings import Settings


@pytest.fixture
def settings():
    return Settings()


# test_engine = create_async_engine(url="postgresql+asyncpg://postgres:password@localhost:5433/pomodoro-test", future=True,
#                              echo=True, pool_pre_ping=True)
#
# AsyncSessionFactory = async_sessionmaker(
#     test_engine,
#     autoflush=False,
#     expire_on_commit=False,
# )
#
#
# @pytest_asyncio.fixture(scope="function")
# async def init_models(event_loop):
#     async with test_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     yield
#     async with test_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#
#
# @pytest_asyncio.fixture(scope="function")
# async def get_db_session() -> AsyncSession:
#     yield AsyncSessionFactory()

@pytest_asyncio.fixture(scope="function")
async def init_models():
    engine = create_async_engine(
        url="postgresql+asyncpg://postgres:password@localhost:5433/pomodoro-test",
        future=True,
        echo=True,
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest_asyncio.fixture(scope="function")
async def get_db_session(init_models) -> AsyncSession:
    engine = init_models
    factory = async_sessionmaker(engine, autoflush=False, expire_on_commit=False)
    yield factory()