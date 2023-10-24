from bson.objectid import ObjectId
from server.database import *
from .state_serializer import deserialize_state


async def retrieve_states():
    cursor = state_collection.find()
    results = await cursor.to_list(None)
    states = [deserialize_state(result) for result in results]
    return states

# Retrieve a state with a matching ID


async def retrieve_state(id: str) -> dict:
    state = await state_collection.find_one({"_id": ObjectId(id)})

    if state:
        return deserialize_state(state)


async def add_state(data: dict) -> dict:
    state = await state_collection.insert_one(data)
    new_state = await state_collection.find_one({"_id": state.inserted_id})
    return deserialize_state(new_state)

# Update a state with a matching ID


async def update_state(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    state = await state_collection.find_one({"_id": ObjectId(id)})

    if state:
        updated_state = await state_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )

        if updated_state:
            return True

    return False

# Delete a state from the database


async def delete_state(id: str):
    state = await state_collection.find_one({"_id": ObjectId(id)})

    if state:
        await state_collection.delete_one({"_id": ObjectId(id)})
        return True
