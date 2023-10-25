from typing import Optional
from pydantic import BaseModel, Field
from ..common.types import PyObjectId


class StateSchema(BaseModel):
    id: PyObjectId = Field(alias='_id')
    name: str = Field(...)
    description: str = Field(None)
    country_id: str = Field(...)

    model_config = {
        'arbitrary_types_allowed': True,
        "json_schema_extra": {
            "example": {
                "name": "Lagos",
                "description": "The economic capital of Nigeria",
                "country_id": "Country ID"
            }
        },
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


class UpdateStateDto(BaseModel):
    name: Optional[str]
    description: Optional[str]

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Lagos",
                "description": "The economic capital of Nigeria",
                "country_id": "Country Id"
            }
        }
    }
