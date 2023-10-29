from datetime import datetime
from pydantic import BaseModel, Field
from ..common.types import PyObjectId
from ..common.schema import Nutrient


class MicroNutrientSchema(Nutrient):
    id: PyObjectId = Field(alias='_id')
    macro_nutrient_id: str = Field(...)
    created_at: datetime | None = Field(datetime.now())
    updated_at: datetime | None = Field(datetime.now())

    model_config = {
        'arbitrary_types_allowed': True,
        "json_schema_extra": {
            "example": {
                "name": "Carbohydrate",
                "description": "Energy foods",
                "macro_nutrient_id": "653c159307e807c4b9b52a98",
                "created_at": str(datetime.now()),
                "updated_at": str(datetime.now())
            }
        },
    }


class CreateMicroNutrientDto(BaseModel):
    name: str = Field(...)
    description: str = Field(None)
    macro_nutrient_id: str = Field(None)
    created_at: datetime | None = Field(datetime.now())
    updated_at: datetime | None = Field(datetime.now())

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Carbohydrate",
                "description": "Energy foods",
                "macro_nutrient_id": "653c159307e807c4b9b52a98",
                "created_at": str(datetime.now()),
                "updated_at": str(datetime.now())
            }
        },
    }


class UpdateMicroNutrientDto(BaseModel):
    name: str | None = Field(None)
    description: str | None = Field(None)
    updated_at: datetime | None = Field(datetime.now())

    model_config = {
        "json_schema_extra": {
            "example": {
                "description": "Energy foods",
                "macro_nutrient_id": "Country Id"
            }
        }
    }
