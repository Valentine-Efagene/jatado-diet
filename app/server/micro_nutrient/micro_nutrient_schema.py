from typing import Optional
from pydantic import BaseModel, Field
from ..common.types import PyObjectId


class MicroNutrientSchema(BaseModel):
    id: PyObjectId = Field(alias='_id')
    name: str = Field(...)
    description: str = Field(None)
    macro_nutrient_id: str = Field(...)

    model_config = {
        'arbitrary_types_allowed': True,
        "json_schema_extra": {
            "example": {
                "name": "Carbohydrate",
                "description": "Energy foods",
                "macro_nutrient_id": "653c159307e807c4b9b52a98"
            }
        },
    }


class CreateMicroNutrientDto(BaseModel):
    name: str = Field(...)
    description: str = Field(None)
    macro_nutrient_id: str = Field(None)

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Carbohydrate",
                "description": "Energy foods",
                "macro_nutrient_id": "653c159307e807c4b9b52a98"
            }
        },
    }


class UpdateMicroNutrientDto(BaseModel):
    name: Optional[str]
    description: Optional[str]

    model_config = {
        "json_schema_extra": {
            "example": {
                "description": "Energy foods",
                "macro_nutrient_id": "Country Id"
            }
        }
    }
