from pydantic import BaseModel, Field
from ..common.types import PyObjectId


class Language(BaseModel):
    id: PyObjectId = Field(alias='_id')
    name: str = Field(...)
    description: str = Field(None)
    ethnicity_id: str = Field(None)

    model_config = {
        'arbitrary_types_allowed': True,
        'json_schema_extra': {
            "example": {
                "name": "Urhobo",
                "description": "A language",
                "ethnicity_id": "Ethnicity ID"
            },
        },
    }


class CreateLanguageDto(BaseModel):
    name: str = Field(...)
    description: str = Field(None)
    ethnicity_id: str = Field(None)

    model_config = {
        'arbitrary_types_allowed': True,
        'json_schema_extra': {
            "example": {
                "name": "Urhobo",
                "description": "A language",
                "ethnicity_id": "Ethnicity ID"
            },
        },
    }


class UpdateLanguageDto(BaseModel):
    name: str | None = Field(None)
    description: str | None = Field(None)
    ethnicity_id: str | None = Field(None)

    model_config: {
        'schema_extra': {
            "example": {
                "name": "Urhobo",
                "description": "A popular language in Delta",
                "ethnicity_id": "Ethnicity ID"
            }
        }}
