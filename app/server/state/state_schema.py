from typing import Optional
from pydantic import BaseModel, Field
from server.common.types import PyObjectId


class StateSchema(BaseModel):
    id: PyObjectId = Field(alias='_id')
    name: str = Field(...)
    description: str = Field(None)
    country_id: str = Field(None)

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Lagos",
                "description": "The economic capital of Nigeria",
                "country_id": "Country Id"
            }
        },
        'arbitrary_types_allowed': True,
    }


class CreateStateDto(BaseModel):
    name: str = Field(...)
    description: str = Field(None)
    country_id: str = Field(None)

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Lagos",
                "description": "The economic capital of Nigeria",
                "country_id": "Country Id"
            }
        },
    }


class UpdateStateModel(BaseModel):
    name: Optional[str]
    description: Optional[str]

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Lagos",
                "description": "The economic capital of Nigeria",
            }
        }
    }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
