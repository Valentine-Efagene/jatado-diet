from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from .country_service import (
    add_country,
    delete_country,
    retrieve_country,
    retrieve_countries,
    update_country,
)

from .country_schema import (
    ErrorResponseModel,
    ResponseModel,
    CountrySchema,
    CreateCountryDto,
    UpdateCountryModel,
)

router = APIRouter()


@router.post("/", response_description="Country data added into the database")
async def add_country_data(country: CreateCountryDto = Body(...)):
    country = jsonable_encoder(country)
    new_country = await add_country(country)
    return ResponseModel(new_country, "Country added successfully.")


@router.get("/{id}", response_description="Country data retrieved")
async def get_country_data(id):
    country = await retrieve_country(id)

    if country:
        return ResponseModel(country, "Country data retrieved successfully")

    return ErrorResponseModel("An error occurred.", 404, "Country doesn't exist.")


@router.get("/", response_description="Countries retrieved")
async def get_countries():
    countries = await retrieve_countries()

    if countries:
        return ResponseModel(countries, "Countries data retrieved successfully")

    return ResponseModel(countries, "Empty list returned")


@router.put("/{id}")
async def update_country_data(id: str, req: UpdateCountryModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
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
