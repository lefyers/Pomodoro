import pytest
import pytest_asyncio

from app.dependency import get_broker_producer
from app.settings import Settings
from app.users.auth.client import MailClient
from app.users.auth.service import AuthService
from app.users.user_profile.repository import UserRepository


class FakeBrokerProducer:
    async def send_welcome_email(self, email_data):
        pass

@pytest_asyncio.fixture
async def mock_auth_service(yandex_client, google_client, fake_user_repository):
    return AuthService(
        user_repository=fake_user_repository,
        settings=Settings(),
        google_client=google_client,
        yandex_client=yandex_client,
        mail_client=MailClient(
            settings=Settings(),
            broker_producer=FakeBrokerProducer(),
        )
    )


@pytest_asyncio.fixture(scope="function")
async def auth_service(yandex_client, google_client, get_db_session, init_models):
    return AuthService(
        user_repository=UserRepository(db_session=get_db_session),
        settings=Settings(),
        google_client=google_client,
        yandex_client=yandex_client,
        mail_client=MailClient(
            settings=Settings(),
            broker_producer=await get_broker_producer(),
        )
    )
