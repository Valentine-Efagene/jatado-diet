from fastapi import APIRouter, Body, Depends
from ..common.schema import ResponseModel, ErrorResponseModel, ListQueryParams
from ..common.serializer import serialize
from ..common.services import retrieve_list
from ..database import macro_nutrient_collection
from .macro_nutrient_helper import deserialize_macro_nutrient

from .macro_nutrient_service import (
    add_macro_nutrient,
    delete_macro_nutrient,
    retrieve_macro_nutrient,
    update_macro_nutrient,
)

from .macro_nutrient_schema import (
    CreateMacroNutrientDto,
    UpdateMacroNutrientDto,
)


router = APIRouter()


@router.post("/", response_description="MacroNutrient data added into the database")
async def add_macro_nutrient_data(macro_nutrient: CreateMacroNutrientDto = Body(...)):
    macro_nutrient = serialize(macro_nutrient)
    new_macro_nutrient = await add_macro_nutrient(macro_nutrient)
    return ResponseModel(new_macro_nutrient, "MacroNutrient added successfully.")


@router.get("/{id}", response_description="MacroNutrient data retrieved")
async def get_macro_nutrient_data(id):
    macro_nutrient = await retrieve_macro_nutrient(id)

    if macro_nutrient:
        return ResponseModel(macro_nutrient, "MacroNutrient data retrieved successfully")

    return ErrorResponseModel("An error occurred.", 404, "MacroNutrient doesn't exist.")


@router.get("/", response_description="Macro Nutrients retrieved")
async def get_macro_nutrients(params: ListQueryParams = Depends()):
    macro_nutrients = await retrieve_list(params, macro_nutrient_collection, deserialize_macro_nutrient)

    if macro_nutrients:
        return ResponseModel(macro_nutrients, "Macro Nutrients data retrieved successfully")

    return ResponseModel(macro_nutrients, "Empty list returned")


@router.put("/{id}")
async def update_macro_nutrient_data(id: str, req: UpdateMacroNutrientDto = Body(...)):
    req = {k: v for k, v in req.model_dump().items() if v is not None}
    updated_macro_nutrient = await update_macro_nutrient(id, req)

    if updated_macro_nutrient:
        return ResponseModel(
            "MacroNutrient with ID: {} name update is successful".format(id),
            "MacroNutrient name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", response_description="MacroNutrient data deleted from the database")
async def delete_macro_nutrient_data(id: str):
    deleted_macro_nutrient = await delete_macro_nutrient(id)
    if deleted_macro_nutrient:
        return ResponseModel(
            "MacroNutrient with ID: {} removed".format(
                id), "MacroNutrient deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "MacroNutrient with id {0} doesn't exist".format(
            id)
    )
