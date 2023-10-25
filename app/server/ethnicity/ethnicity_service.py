from bson.objectid import ObjectId
from ..database import *
from .ethnicity_serializer import deserialize_ethnicity


async def retrieve_ethnicities():
    cursor = ethnicity_collection.find()
    results = await cursor.to_list(None)
    ethnicitys = [deserialize_ethnicity(result) for result in results]
    return ethnicitys

# Retrieve a ethnicity with a matching ID


async def retrieve_ethnicity(id: str) -> dict:
    ethnicity = await ethnicity_collection.find_one({"_id": ObjectId(id)})

    if ethnicity:
        return deserialize_ethnicity(ethnicity)


async def add_ethnicity(data: dict) -> dict:
    ethnicity = await ethnicity_collection.insert_one(data)
    new_ethnicity = await ethnicity_collection.find_one({"_id": ethnicity.inserted_id})
    return deserialize_ethnicity(new_ethnicity)

# Update a ethnicity with a matching ID


async def update_ethnicity(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    ethnicity = await ethnicity_collection.find_one({"_id": ObjectId(id)})

    if ethnicity:
        updated_ethnicity = await ethnicity_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )

        if updated_ethnicity:
            return True

    return False

# Delete a ethnicity from the database


async def delete_ethnicity(id: str):
    ethnicity = await ethnicity_collection.find_one({"_id": ObjectId(id)})

    if ethnicity:
        await ethnicity_collection.delete_one({"_id": ObjectId(id)})
        return True
