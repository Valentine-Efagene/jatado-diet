from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorDatabase

MONGO_DETAILS = "mongodb://localhost:27017"
client: AsyncIOMotorClient = AsyncIOMotorClient(MONGO_DETAILS)
database: AsyncIOMotorDatabase = client.diet

country_collection = database.get_collection("countries")
state_collection = database.get_collection("states")
lga_collection = database.get_collection("lgas")
