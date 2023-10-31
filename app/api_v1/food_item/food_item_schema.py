from datetime import datetime
from pydantic import BaseModel, Field
from typing import List
from ..common.schema import Nutrient
from ..common.types import PyObjectId


class Name(BaseModel):
    language_id: str
    name: str


class FoodItem(BaseModel):
    id: PyObjectId = Field(alias='_id')
    name: str = Field(...)
    description: str = Field(None)
    names: List[Name] = Field([])
    nutrients: List[Nutrient] = Field([])
    created_at: datetime | None = Field(datetime.now())
    updated_at: datetime | None = Field(datetime.now())

    model_config = {
        'arbitrary_types_allowed': True,
        'json_schema_extra': {
            "example": {
                "name": "Nigeria",
                "description": "Most populous nation in Africa",
            },
        },
    }


class NutrientAndQuantity:
    nutrient_id: str
    quantity: float


class NutrientHydratedAndQuantity:
    nutrient: Nutrient
    quantity: float


class CreateFoodItemDto(BaseModel):
    name: str = Field(...)
    description: str = Field(None)
    quantity: int = Field(...)
    names: List[Name] = Field([])
    nutrients: List[Nutrient] = Field([])
    created_at: datetime | None = Field(datetime.now())
    updated_at: datetime | None = Field(datetime.now())

    model_config = {
        'arbitrary_types_allowed': True,
        'json_schema_extra': {
            "example": {
                "name": "Nigeria",
                "description": "Most populous nation in Africa",
            },
        },
    }


class UpdateFoodItemDto(BaseModel):
    name: str | None = Field(None)
    description: str | None = Field(None)
    updated_at: datetime | None = Field(datetime.now())

    model_config: {
        'schema_extra': {
            "example": {
                "name": "Nigeria",
                "description": "Most populous nation in Africa",
            }
        }}
