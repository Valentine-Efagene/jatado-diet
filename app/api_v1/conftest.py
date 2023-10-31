import pytest_asyncio
import pytest
from fastapi.testclient import TestClient
import os
from .database import get_database_and_client
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from .app import create_application

from .database import client as db_client, db_name
from .config import settings
from .auth.auth_service import mock_get_current_user, get_current_user
from .auth.auth_schema import mock_oauth2_scheme, oauth2_scheme

# Use pytest-asyncio fixture manager
pytestmark = pytest.mark.asyncio


@pytest_asyncio.fixture(scope="session", autouse=True)
def env_setup():
    os.environ["ENV"] = 'test'


@pytest_asyncio.fixture(scope="session", autouse=True)
def test_client(env_setup):
    if (db_name != settings.mongodb_test_db_name):
        raise Exception('You are not using the test Database')

    app = create_application()

    with TestClient(app) as test_client:
        app.dependency_overrides[oauth2_scheme] = mock_oauth2_scheme
        app.dependency_overrides[get_current_user] = mock_get_current_user
        yield test_client
        db_client.drop_database(db_name)


@pytest_asyncio.fixture()
async def mongo_client():
    env = settings.environment
    client: AsyncIOMotorClient
    database: AsyncIOMotorDatabase
    [client, database] = get_database_and_client(env)
    yield client
