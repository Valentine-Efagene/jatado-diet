from typing import Annotated
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ..user.user_schema import User, UserInDB
from ..common.schema import ResponseModel

from .auth_service import (
    fake_hash_password,
)

from ..user.user_service import (
    fake_users_db
)


router = APIRouter()


@router.post("/")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)

    if not user_dict:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")

    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")

    return ResponseModel(data={"access_token": user.username, "token_type": "bearer"}, message='Logged In')
