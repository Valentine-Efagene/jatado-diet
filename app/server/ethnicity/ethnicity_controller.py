from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from ..common.schema import ResponseModel, ErrorResponseModel

from .ethnicity_service import (
    add_ethnicity,
    delete_ethnicity,
    retrieve_ethnicity,
    retrieve_ethnicities,
    update_ethnicity,
)

from .ethnicity_schema import (
    CreateEthnicityDto,
    UpdateEthnicityDto,
)


router = APIRouter()


@router.post("/", response_description="ethnicity data added into the database")
async def add_ethnicity_data(ethnicity: CreateEthnicityDto = Body(...)):
    ethnicity = jsonable_encoder(ethnicity)
    new_ethnicity = await add_ethnicity(ethnicity)
    return ResponseModel(new_ethnicity, "ethnicity added successfully.")


@router.get("/", response_description="ethnicities retrieved")
async def get_ethnicities():
    countries = await retrieve_ethnicities()

    if countries:
        return ResponseModel(countries, "ethnicitys data retrieved successfully")

    return ResponseModel(countries, "Empty list returned")


@router.get("/{id}", response_description="ethnicity data retrieved")
async def get_ethnicity_data(id):
    ethnicity = await retrieve_ethnicity(id)

    if ethnicity:
        return ResponseModel(ethnicity, "ethnicity data retrieved successfully")

    return ErrorResponseModel("An error occurred.", 404, "ethnicity doesn't exist.")


@router.put("/{id}")
async def update_ethnicity_data(id: str, req: UpdateEthnicityDto = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_ethnicity = await update_ethnicity(id, req)

    if updated_ethnicity:
        return ResponseModel(
            "ethnicity with ID: {} name update is successful".format(id),
            "ethnicity name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", response_description="ethnicity data deleted from the database")
async def delete_ethnicity_data(id: str):
    deleted_ethnicity = await delete_ethnicity(id)
    if deleted_ethnicity:
        return ResponseModel(
            "ethnicity with ID: {} removed".format(
                id), "ethnicity deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "ethnicity with id {0} doesn't exist".format(
            id)
    )
