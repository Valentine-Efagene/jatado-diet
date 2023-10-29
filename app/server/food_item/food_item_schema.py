from datetime import datetime
from pydantic import BaseModel, Field
from ..common.types import PyObjectId


class FoodItem(BaseModel):
    id: PyObjectId = Field(alias='_id')
    name: str = Field(...)
    description: str = Field(None)
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


class FoodItemAndQuantity:
    food_item_id: str
    quantity: float
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_at: datetime | None = Field(datetime.now())
    updated_at: datetime | None = Field(datetime.now())


class FoodItemHydratedAndQuantity:
    food_item: FoodItem
    quantity: float
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_at: datetime | None = Field(datetime.now())
    updated_at: datetime | None = Field(datetime.now())


class CreateFoodItemDto(BaseModel):
    name: str = Field(...)
    description: str = Field(None)
    quantity: int = Field(...)
    food_item: FoodItem = Field(...)
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
