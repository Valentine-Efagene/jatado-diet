
from dataclasses import dataclass
from fastapi import Query
from pydantic import BaseModel, Field
from .types import PyObjectId


def ResponseModel(data, message, code: int = 200):
    return {
        "data": data,
        "code": code,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}


@dataclass
class ListQueryParams:
    page: int | None = Query(None, description="Page number")
    limit: int | None = Query(None, description="Number of items per page")
    keyword: str | None = Query(None, description="Keyword to search by")


class Nutrient(BaseModel):
    id: PyObjectId = Field(alias='_id')
    name: str = Field(...)
    description: str = Field(None)

    model_config = {
        'arbitrary_types_allowed': True,
        'json_schema_extra': {
            "example": {
                "name": "Carbohydrate",
                "description": "Energy foods",
            },
        },
    }
