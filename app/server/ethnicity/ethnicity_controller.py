from fastapi import APIRouter, Body
from ..common.serializer import serialize
from ..common.schema import ResponseModel, ErrorResponseModel
from ..common.services import retrieve_list
from ..common.schema import ListQueryParams
from ..database import ethnicity_collection
from .ethnicity_helper import deserialize_ethnicity

from .ethnicity_service import (
    add_ethnicity,
    delete_ethnicity,
    retrieve_ethnicity,
    update_ethnicity,
)

from .ethnicity_schema import (
    CreateEthnicityDto,
    UpdateEthnicityDto,
)


router = APIRouter()


@router.post("/", response_description="ethnicity data added into the database")
async def add_ethnicity_data(ethnicity: CreateEthnicityDto = Body(...)):
    ethnicity = serialize(ethnicity)
    new_ethnicity = await add_ethnicity(ethnicity)
    return ResponseModel(new_ethnicity, "ethnicity added successfully.")


@router.get("/", response_description="ethnicities retrieved")
async def get_ethnicities(params: ListQueryParams):
    countries = await retrieve_list(params=params, collection=ethnicity_collection, deserialize=deserialize_ethnicity)

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
    req = {k: v for k, v in req.model_dump().items() if v is not None}
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
