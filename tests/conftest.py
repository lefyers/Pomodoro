import asyncio

import pytest
from sqlalchemy.ext.asyncio import create_async_engine

pytest_plugins = [
    "tests.fixtures.auth.auth_service",
    "tests.fixtures.auth.clients",
    "tests.fixtures.users.user_repository",
    "tests.fixtures.infrastructure",
    "tests.fixtures.users.user_model",
]


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
