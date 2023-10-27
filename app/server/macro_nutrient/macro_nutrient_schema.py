from typing import Optional
from pydantic import BaseModel, Field
from ..common.types import PyObjectId


class MacroNutrientSchema(BaseModel):
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


class CreateMacroNutrientDto(BaseModel):
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


class UpdateMacroNutrientDto(BaseModel):
    name: str | None = Field(None)
    description: str | None = Field(None)

    model_config: {
        'schema_extra': {
            "example": {
                "name": "Carbohydrate",
                "description": "Energy foods",
            }
        }}