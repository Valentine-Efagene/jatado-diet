from bson.objectid import ObjectId
from ..database import *
from .language_serializer import deserialize_language


async def retrieve_languages():
    cursor = language_collection.find()
    results = await cursor.to_list(None)
    languages = [deserialize_language(result) for result in results]
    return languages

# Retrieve a language with a matching ID


async def retrieve_language(id: str) -> dict:
    language = await language_collection.find_one({"_id": ObjectId(id)})

    if language:
        return deserialize_language(language)


async def add_language(data: dict) -> dict:
    language = await language_collection.insert_one(data)
    new_language = await language_collection.find_one({"_id": language.inserted_id})
    return deserialize_language(new_language)

# Update a language with a matching ID


async def update_language(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    language = await language_collection.find_one({"_id": ObjectId(id)})

    if language:
        updated_language = await language_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )

        if updated_language:
            return True

    return False

# Delete a language from the database


async def delete_language(id: str):
    language = await language_collection.find_one({"_id": ObjectId(id)})

    if language:
        await language_collection.delete_one({"_id": ObjectId(id)})
        return True
