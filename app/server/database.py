import os
from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorDatabase
from .config import settings

env = settings.environment


def get_database() -> AsyncIOMotorDatabase:
    if env == 'DEVELOPMENT':
        return AsyncIOMotorClient(settings.mongodb_dev_uri)[settings.mongodb_dev_db_name]
    elif env == 'PRODUCTION':
        return AsyncIOMotorClient(settings.mongodb_prod_uri)[settings.mongodb_prod_db_name]
    else:
        return AsyncIOMotorClient(settings.mongodb_test_uri)[settings.mongodb_test_db_name]


database: AsyncIOMotorDatabase = get_database()
country_collection = database.get_collection("countries")
state_collection = database.get_collection("states")
lga_collection = database.get_collection("lgas")
ethnicity_collection = database.get_collection("ethnicities")
