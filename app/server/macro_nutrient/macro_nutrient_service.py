from bson.objectid import ObjectId
from ..database import *
from .macro_nutrient_helper import deserialize_macro_nutrient


# Retrieve a macro_nutrient with a matching ID


async def retrieve_macro_nutrient(id: str) -> dict:
    macro_nutrient = await macro_nutrient_collection.find_one({"_id": ObjectId(id)})

    if macro_nutrient:
        return deserialize_macro_nutrient(macro_nutrient)


async def add_macro_nutrient(data: dict) -> dict:
    macro_nutrient = await macro_nutrient_collection.insert_one(data)
    new_macro_nutrient = await macro_nutrient_collection.find_one({"_id": macro_nutrient.inserted_id})
    return deserialize_macro_nutrient(new_macro_nutrient)

# Update a macro_nutrient with a matching ID


async def update_macro_nutrient(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    macro_nutrient = await macro_nutrient_collection.find_one({"_id": ObjectId(id)})

    if macro_nutrient:
        updated_macro_nutrient = await macro_nutrient_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )

        if updated_macro_nutrient:
            return True

    return False

# Delete a macro_nutrient from the database


async def delete_macro_nutrient(id: str):
    macro_nutrient = await macro_nutrient_collection.find_one({"_id": ObjectId(id)})

    if macro_nutrient:
        await macro_nutrient_collection.delete_one({"_id": ObjectId(id)})
        return True
