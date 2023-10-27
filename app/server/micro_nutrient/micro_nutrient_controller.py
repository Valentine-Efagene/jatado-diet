from fastapi import APIRouter, Body, Depends
from ..common.serializer import serialize
from ..common.schema import ListQueryParams
from ..common.services import retrieve_list
from ..database import micro_nutrient_collection
from .micro_nutrient_helper import deserialize_micro_nutrient

from .micro_nutrient_service import (
    add_micro_nutrient,
    delete_micro_nutrient,
    retrieve_micro_nutrient,
    update_micro_nutrient,
)

from .micro_nutrient_schema import (
    CreateMicroNutrientDto,
    UpdateMicroNutrientDto,
)


from ..common.schema import ResponseModel, ErrorResponseModel

router = APIRouter()


@router.post("/", response_description="MicroNutrient data added into the database")
async def add_micro_nutrient_data(micro_nutrient: CreateMicroNutrientDto = Body(...)):
    micro_nutrient = serialize(micro_nutrient)
    new_micro_nutrient = await add_micro_nutrient(micro_nutrient)
    return ResponseModel(new_micro_nutrient, "micro_nutrient added successfully.")


@router.get("/", response_description="MicroNutrients retrieved")
async def get_micro_nutrients(params: ListQueryParams = Depends()):
    micro_nutrients = await retrieve_list(params=params, collection=micro_nutrient_collection, deserialize=deserialize_micro_nutrient)

    if micro_nutrients:
        return ResponseModel(micro_nutrients, "MicroNutrients data retrieved successfully")

    return ResponseModel(micro_nutrients, "Empty list returned")


@router.get("/{id}", response_description="micro_nutrient data retrieved")
async def get_micro_nutrient_data(id):
    micro_nutrient = await retrieve_micro_nutrient(id)

    if micro_nutrient:
        return ResponseModel(micro_nutrient, "micro_nutrient data retrieved successfully")

    return ErrorResponseModel("An error occurred.", 404, "micro_nutrient doesn't exist.")


@router.put("/{id}")
async def update_micro_nutrient_data(id: str, req: UpdateMicroNutrientDto = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_micro_nutrient = await update_micro_nutrient(id, req)

    if updated_micro_nutrient:
        return ResponseModel(
            "micro_nutrient with ID: {} name update is successful".format(id),
            "micro_nutrient name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", response_description="micro_nutrient data deleted from the database")
async def delete_micro_nutrient_data(id: str):
    deleted_micro_nutrient = await delete_micro_nutrient(id)
    if deleted_micro_nutrient:
        return ResponseModel(
            "micro_nutrient with ID: {} removed".format(
                id), "micro_nutrient deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "micro_nutrient with id {0} doesn't exist".format(
            id)
    )