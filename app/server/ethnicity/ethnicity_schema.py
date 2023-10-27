from typing import Optional
from pydantic import BaseModel, Field
from ..common.types import PyObjectId


class EthnicitySchema(BaseModel):
    id: PyObjectId = Field(alias='_id')
    name: str = Field(...)
    description: str = Field(None)
    lga_id: str = Field(None)

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Waffirians",
                "description": "People of Warri",
                "lga_id": "653a2e485c3ed608fd5c6d13"
            }
        },
        'arbitrary_types_allowed': True,
    }


class CreateEthnicityDto(BaseModel):
    name: str = Field(...)
    description: str = Field(None)
    lga_id: str = Field(None)

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Waffirians",
                "description": "People of Warri",
                "lga_id": "653a2e485c3ed608fd5c6d13"
            }
        },
    }


class UpdateEthnicityDto(BaseModel):
    name: str | None = Field(None)
    description: str | None = Field(None)

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Waffirians",
                "description": "People of Warri",
                "lga_id": "653a2e485c3ed608fd5c6d13",
            }
        }
    }
