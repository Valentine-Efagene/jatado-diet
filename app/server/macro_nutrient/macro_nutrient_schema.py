from datetime import datetime
from pydantic import BaseModel, Field
from ..common.schema import Nutrient


class MacroNutrient(Nutrient):
    pass


class CreateMacroNutrientDto(BaseModel):
    name: str = Field(...)
    description: str = Field(None)
    created_at: datetime | None = Field(datetime.now())
    updated_at: datetime | None = Field(datetime.now())

    model_config = {
        'arbitrary_types_allowed': True,
        'json_schema_extra': {
            "example": {
                "name": "Carbohydrate",
                "description": "Energy foods",
                "created_at": str(datetime.now()),
                "updated_at": str(datetime.now())
            },
        },
    }


class UpdateMacroNutrientDto(BaseModel):
    name: str | None = Field(None)
    description: str | None = Field(None)
    updated_at: datetime | None = Field(datetime.now())

    model_config: {
        'schema_extra': {
            "example": {
                "name": "Carbohydrate",
                "description": "Energy foods",
            }
        }}
