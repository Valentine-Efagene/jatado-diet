from datetime import datetime
from pydantic import BaseModel, Field
from typing import List
from ..common.schema import Name
from ..common.types import PyObjectId, Type


class RecipeUnitScheme(BaseModel):
    id: PyObjectId = Field(alias='_id')
    name: str = Field(...)
    names: List[Name] = Field([])
    options: List[Type] = Field([])
    description: str = Field(None)
    created_at: datetime | None = Field(datetime.now())
    updated_at: datetime | None = Field(datetime.now())

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Ethiope East",
                "description": "Has a RecipeUnitScheme university (DELSU)",
                "state_id": "State ID",
                "created_at": str(datetime.now()),
                "updated_at": str(datetime.now())
            }
        },
        'arbitrary_types_allowed': True,
    }


class CreateRecipeUnitSchemeDto(BaseModel):
    name: str = Field(...)
    description: str = Field(None)
    options: List[Type] = Field([])
    names: List[Name] = Field([])
    created_at: datetime | None = Field(datetime.now())
    updated_at: datetime | None = Field(datetime.now())

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Lagos",
                "description": "The economic capital of Nigeria",
                "state_id": "State ID",
                "created_at": str(datetime.now()),
                "updated_at": str(datetime.now())
            }
        },
    }


class UpdateRecipeUnitSchemeDto(BaseModel):
    name: str | None = Field(None)
    description: str | None = Field(None)
    options: List[Type] | None = Field([])
    names: List[Name] | None = Field([])
    updated_at: datetime | None = Field(datetime.now())

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Lagos",
                "description": "The economic capital of Nigeria",
                "recipe_unit_scheme_id": "recipe_unit_scheme ID",
            }
        }
    }
