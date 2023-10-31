from bson.objectid import ObjectId
from ..database import *
from ..common.serializer import serialize
from .micro_nutrient_helper import deserialize_micro_nutrient


# Retrieve a micro_nutrient with a matching ID


async def retrieve_micro_nutrient(id: str) -> dict:
    micro_nutrient = await micro_nutrient_collection.find_one({"_id": ObjectId(id)})

    if micro_nutrient:
        return deserialize_micro_nutrient(micro_nutrient)


async def add_micro_nutrient(data: dict) -> dict:
    micro_nutrient = await micro_nutrient_collection.insert_one(data)
    new_micro_nutrient = await micro_nutrient_collection.find_one({"_id": micro_nutrient.inserted_id})
    return deserialize_micro_nutrient(new_micro_nutrient)

# Update a micro_nutrient with a matching ID


async def update_micro_nutrient(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    micro_nutrient = await micro_nutrient_collection.find_one({"_id": ObjectId(id)})

    if micro_nutrient:
        updated_micro_nutrient = await micro_nutrient_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )

        if updated_micro_nutrient:
            return True

    return False

# Delete a micro_nutrient from the database


async def delete_micro_nutrient(id: str):
    micro_nutrient = await micro_nutrient_collection.find_one({"_id": ObjectId(id)})

    if micro_nutrient:
        await micro_nutrient_collection.delete_one({"_id": ObjectId(id)})
        return True
