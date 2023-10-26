import pytest_asyncio
from fastapi.testclient import TestClient
import os

from .database import client as db_client, db_name
from .config import settings
from app.server.app import app


@pytest_asyncio.fixture(scope="session", autouse=True)
def env_setup():
    os.environ["ENV"] = 'test'


@pytest_asyncio.fixture(scope="session", autouse=True)
def test_client(env_setup):
    if (db_name != settings.mongodb_test_db_name):
        raise Exception('You are not using the test Database')

    with TestClient(app) as test_client:
        yield test_client
        db_client.drop_database(db_name)
