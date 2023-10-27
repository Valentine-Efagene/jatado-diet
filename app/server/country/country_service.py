from bson.objectid import ObjectId
from ..database import *
from .country_helper import deserialize_country
from ..common.schema import ListQueryParams


async def retrieve_countries(params: ListQueryParams):
    page = params.page
    limit = params.limit
    keyword = params.keyword

    resPerPage = int(limit) if limit else int(
        settings.pagination_limit)
    currentPage = int(page) if page else 1
    skip = resPerPage * (currentPage - 1)

    search = {
        "name": {
            "$regex": keyword,
            "$options": 'i',
        },
    } if keyword else {}

    cursor = country_collection.find(search).limit(resPerPage).skip(skip)
    results = await cursor.to_list(None)
    countries = [deserialize_country(result) for result in results]
    return countries

# Retrieve a country with a matching ID


async def retrieve_country(id: str) -> dict:
    country = await country_collection.find_one({"_id": ObjectId(id)})

    if country:
        return deserialize_country(country)


async def add_country(data: dict) -> dict:
    country = await country_collection.insert_one(data)
    new_country = await country_collection.find_one({"_id": country.inserted_id})
    return deserialize_country(new_country)

# Update a country with a matching ID


async def update_country(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    country = await country_collection.find_one({"_id": ObjectId(id)})

    if country:
        updated_country = await country_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )

        if updated_country:
            return True

    return False

# Delete a country from the database


async def delete_country(id: str):
    country = await country_collection.find_one({"_id": ObjectId(id)})

    if country:
        await country_collection.delete_one({"_id": ObjectId(id)})
        return True
