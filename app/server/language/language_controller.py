from fastapi import APIRouter, Body, Depends
from ..common.serializer import serialize
from ..common.services import retrieve_list
from ..database import language_collection
from ..common.schema import ListQueryParams
from ..common.schema import ResponseModel, ErrorResponseModel
from .language_helper import deserialize_language

from .language_service import (
    add_language,
    delete_language,
    retrieve_language,
    update_language,
)

from .language_schema import (
    CreateLanguageDto,
    UpdateLanguageDto,
)


router = APIRouter()


@router.post("/", response_description="Language data added into the database")
async def add_language_data(language: CreateLanguageDto = Body(...)):
    language = serialize(language)
    new_language = await add_language(language)
    return ResponseModel(new_language, "Language added successfully.")


@router.get("/{id}", response_description="Language data retrieved")
async def get_language_data(id):
    language = await retrieve_language(id)

    if language:
        return ResponseModel(language, "Language data retrieved successfully")

    return ErrorResponseModel("An error occurred.", 404, "Language doesn't exist.")


@router.get("/", response_description="Languages retrieved")
async def get_languages(params: ListQueryParams = Depends()):
    languages = await retrieve_list(params=params, collection=language_collection, deserialize=deserialize_language)

    if languages:
        return ResponseModel(languages, "Languages data retrieved successfully")

    return ResponseModel(languages, "Empty list returned")


@router.put("/{id}")
async def update_language_data(id: str, req: UpdateLanguageDto = Body(...)):
    req = {k: v for k, v in req.model_dump().items() if v is not None}
    updated_language = await update_language(id, req)

    if updated_language:
        return ResponseModel(
            "Language with ID: {} name update is successful".format(id),
            "Language name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", response_description="Language data deleted from the database")
async def delete_language_data(id: str):
    deleted_language = await delete_language(id)
    if deleted_language:
        return ResponseModel(
            "Language with ID: {} removed".format(
                id), "Language deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Language with id {0} doesn't exist".format(
            id)
    )
