from typing import Annotated
from fastapi import APIRouter, Body, Depends
from .user_schema import User
from ..common.schema import ResponseModel, ErrorResponseModel, ListQueryParams
from ..common.serializer import serialize
from ..common.services import retrieve_list
from ..database import user_collection
from ..auth.auth_schema import OAuthTokenDeps
from .user_helper import deserialize_user

from .user_service import (
    add_user,
    delete_user,
    retrieve_user,
    update_user,
    get_current_active_user,
)

from .user_schema import (
    CreateUserDto,
    UpdateUserDto,
)


router = APIRouter()


@router.post("/", response_description="User data added into the database")
async def add_user_data(user: CreateUserDto = Body(...)):
    user = serialize(user)
    new_user = await add_user(user)
    return ResponseModel(new_user, "User added successfully.")


@router.get("/me", response_description="User data added into the database")
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user


@router.get("/{id}", response_description="User data retrieved")
async def get_user_data(id):
    user = await retrieve_user(id)

    if user:
        return ResponseModel(user, "User data retrieved successfully")

    return ErrorResponseModel("An error occurred.", 404, "User doesn't exist.")


@router.get("/", response_description="Users retrieved")
async def get_users(token: OAuthTokenDeps, params: ListQueryParams = Depends()):
    users = await retrieve_list(params, user_collection, deserialize_user)

    if users:
        return ResponseModel(users, "Users data retrieved successfully")

    return ResponseModel(users, "Empty list returned")


@router.put("/{id}")
async def update_user_data(id: str, req: UpdateUserDto = Body(...)):
    req = {k: v for k, v in req.model_dump().items() if v is not None}
    updated_user = await update_user(id, req)

    if updated_user:
        return ResponseModel(
            "User with ID: {} name update is successful".format(id),
            "User name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", response_description="User data deleted from the database")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "User with ID: {} removed".format(
                id), "User deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "User with id {0} doesn't exist".format(
            id)
    )