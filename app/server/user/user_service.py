from typing import Annotated
from fastapi import Depends, HTTPException
from bson.objectid import ObjectId
from ..database import *
from .user_schema import User, Status, Role
from .user_helper import deserialize_user
from ..auth.auth_service import get_current_user

fake_users_db = {
    "johndoe": {
        "_id": str(ObjectId()),
        "username": "johndoe",
        "firstName": "John",
        "lastName": "Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "role": Role.STAFF,
        "status": Status.ACTIVE,
    },
    "alice": {
        "_id": str(ObjectId()),
        "username": "alice",
        "firstName": "Alice",
        "lastName": "Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "role": Role.STAFF,
        "status": Status.ACTIVE,
    },
}


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.status != Status.ACTIVE:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


# Retrieve a user with a matching ID


async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})

    if user:
        return deserialize_user(user)


async def add_user(data: dict) -> dict:
    user = await user_collection.insert_one(data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return deserialize_user(new_user)

# Update a user with a matching ID


async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    user = await user_collection.find_one({"_id": ObjectId(id)})

    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )

        if updated_user:
            return True

    return False

# Delete a user from the database


async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})

    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True
