from fastapi import APIRouter, Body, Depends
from ..common.schema import ResponseModel, ErrorResponseModel, ListQueryParams
from ..common.serializer import serialize
from ..common.services import retrieve_list
from ..database import country_collection
from .country_helper import deserialize_country

from .country_service import (
    add_country,
    delete_country,
    retrieve_country,
    update_country,
)

from .country_schema import (
    CreateCountryDto,
    UpdateCountryDto,
)


router = APIRouter()


@router.post("/", response_description="Country data added into the database")
async def add_country_data(country: CreateCountryDto = Body(...)):
    country = serialize(country)
    new_country = await add_country(country)
    return ResponseModel(new_country, "Country added successfully.")


@router.get("/{id}", response_description="Country data retrieved")
async def get_country_data(id):
    country = await retrieve_country(id)

    if country:
        return ResponseModel(country, "Country data retrieved successfully")

    return ErrorResponseModel("An error occurred.", 404, "Country doesn't exist.")


@router.get("/", response_description="Countries retrieved")
async def get_countries(params: ListQueryParams = Depends()):
    countries = await retrieve_list(params, country_collection, deserialize_country)

    if countries:
        return ResponseModel(countries, "Countries data retrieved successfully")

    return ResponseModel(countries, "Empty list returned")


@router.put("/{id}")
async def update_country_data(id: str, req: UpdateCountryDto = Body(...)):
    req = {k: v for k, v in req.model_dump().items() if v is not None}
    updated_country = await update_country(id, req)

    if updated_country:
        return ResponseModel(
            "Country with ID: {} name update is successful".format(id),
            "Country name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", response_description="Country data deleted from the database")
async def delete_country_data(id: str):
    deleted_country = await delete_country(id)
    if deleted_country:
        return ResponseModel(
            "Country with ID: {} removed".format(
                id), "Country deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Country with id {0} doesn't exist".format(
            id)
    )
