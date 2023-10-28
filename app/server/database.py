from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection, AsyncIOMotorDatabase
from .config import settings

env = settings.environment


def get_db_name(env: str) -> AsyncIOMotorDatabase:
    if env == 'DEVELOPMENT':
        return settings.mongodb_dev_db_name
    elif env == 'PRODUCTION':
        return settings.mongodb_prod_db_name
    else:
        return settings.mongodb_test_db_name


def get_database_and_client(env: str) -> AsyncIOMotorDatabase:
    if env == 'DEVELOPMENT':
        client = AsyncIOMotorClient(settings.mongodb_dev_uri)
        database = client[settings.mongodb_dev_db_name]
    elif env == 'PRODUCTION':
        client = AsyncIOMotorClient(settings.mongodb_prod_uri)
        database = client[settings.mongodb_prod_db_name]
    else:
        client = AsyncIOMotorClient(settings.mongodb_test_uri)
        database = client[settings.mongodb_test_db_name]

    return [client, database]


client: AsyncIOMotorClient
database: AsyncIOMotorDatabase
[client, database] = get_database_and_client(env)
db_name = get_db_name(env)

user_collection: AsyncIOMotorCollection = database.get_collection(
    "users")
country_collection: AsyncIOMotorCollection = database.get_collection(
    "countries")
state_collection: AsyncIOMotorCollection = database.get_collection("states")
lga_collection: AsyncIOMotorCollection = database.get_collection("lgas")
ethnicity_collection: AsyncIOMotorCollection = database.get_collection(
    "ethnicities")
language_collection: AsyncIOMotorCollection = database.get_collection(
    "languages")
macro_nutrient_collection: AsyncIOMotorCollection = database.get_collection(
    "macro_nutrients")
micro_nutrient_collection: AsyncIOMotorCollection = database.get_collection(
    "micro_nutrients")
