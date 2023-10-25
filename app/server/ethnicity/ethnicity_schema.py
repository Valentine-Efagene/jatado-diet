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
                "name": "Urhobo",
                "description": "An ethnicity",
                "lga_id": "LGA ID"
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
                "name": "Urhobo",
                "description": "An ethnicity",
                "lga_id": "LGA ID"
            }
        },
    }


class UpdateEthnicityDto(BaseModel):
    name: Optional[str]
    description: Optional[str]

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Urhobo",
                "description": "An ethnicity",
                "lga_id": "LGA ID",
            }
        }
    }
