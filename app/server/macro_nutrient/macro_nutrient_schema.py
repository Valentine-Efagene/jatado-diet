from pydantic import BaseModel, Field
from ..common.schema import Nutrient


class MacroNutrient(Nutrient):
    pass


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
