from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from .lga_service import (
    add_lga,
    delete_lga,
    retrieve_lga,
    retrieve_lgas,
    update_lga,
)

from .lga_schema import (
    ErrorResponseModel,
    ResponseModel,
    CreateLgaDto,
    UpdateLgaDto,
)

router = APIRouter()


@router.post("/", response_description="lga data added into the database")
async def add_lga_data(lga: CreateLgaDto = Body(...)):
    lga = jsonable_encoder(lga)
    new_lga = await add_lga(lga)
    return ResponseModel(new_lga, "lga added successfully.")


@router.get("/", response_description="lgas retrieved")
async def get_lgas():
    countries = await retrieve_lgas()

    if countries:
        return ResponseModel(countries, "lgas data retrieved successfully")

    return ResponseModel(countries, "Empty list returned")


@router.get("/{id}", response_description="lga data retrieved")
async def get_lga_data(id):
    lga = await retrieve_lga(id)

    if lga:
        return ResponseModel(lga, "lga data retrieved successfully")

    return ErrorResponseModel("An error occurred.", 404, "lga doesn't exist.")


@router.put("/{id}")
async def update_lga_data(id: str, req: UpdateLgaDto = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_lga = await update_lga(id, req)

    if updated_lga:
        return ResponseModel(
            "lga with ID: {} name update is successful".format(id),
            "lga name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", response_description="lga data deleted from the database")
async def delete_lga_data(id: str):
    deleted_lga = await delete_lga(id)
    if deleted_lga:
        return ResponseModel(
            "lga with ID: {} removed".format(
                id), "lga deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "lga with id {0} doesn't exist".format(
            id)
    )
