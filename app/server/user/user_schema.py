from enum import Enum
from pydantic import BaseModel, Field
from bson import ObjectId
from ..common.types import PyObjectId


class Role(str, Enum):
    ADMIN = 'ADMIN'
    STAFF = 'STAFF'


class Status(str, Enum):
    ACTIVE = 'ACTIVE'
    SUSPENDED = 'SUSPENDED'


class User(BaseModel):
    id: PyObjectId = Field(alias='_id')
    username: str = Field(...)
    email: str = Field(...)
    firstName: str | None = Field(None)
    lastName: str | None = Field(None)
    role: str = Field(Role.STAFF)
    status: str = Field(Status.ACTIVE)

    model_config = {
        'arbitrary_types_allowed': True,
        'json_schema_extra': {
            "example": {
                "username": str(ObjectId()),
                "email": "janedoe@testmail.com",
                "firstName": "Jane",
                "lastName": "Doe",
            },
        },
    }


class UserInDB(User):
    hashed_password: str

    model_config = {
        'arbitrary_types_allowed': True,
        'json_schema_extra': {
            "example": {
                "_id": str(ObjectId()),
                "username": "jane",
                "email": "janedoe@testmail.com",
                "firstName": "Jane",
                "lastName": "Doe",
                "hashed_password": "576e7a6767b6687f"
            },
        },
    }


class CreateUserDto(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    firstName: str | None = Field(None)
    lastName: str | None = Field(None)
    role: str = Field(Role.STAFF)
    status: str = Field(Status.ACTIVE)

    model_config = {
        'arbitrary_types_allowed': True,
        'json_schema_extra': {
            "example": {
                "username": "jane",
                "email": "janedoe@testmail.com",
                "firstName": "Jane",
                "lastName": "Doe",
            },
        },
    }


class UpdateUserDto(BaseModel):
    username: str | None = Field(...)
    email: str | None = Field(...)
    firstName: str | None = Field(None)
    lastName: str | None = Field(None)
    role: str | None = Field(Role.STAFF)
    status: str | None = Field(Status.ACTIVE)

    model_config: {
        'schema_extra': {
            "example": {
                "username": "jane",
                "email": "janedoe@testmail.com",
                "firstName": "Jane",
                "lastName": "Doe",
            }
        }}