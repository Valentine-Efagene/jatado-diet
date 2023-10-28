
from typing import Annotated
from dataclasses import dataclass
from fastapi import Query, Depends
from fastapi.security import OAuth2PasswordBearer


def ResponseModel(data, message, code: int = 200):
    return {
        "data": data,
        "code": code,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}


@dataclass
class ListQueryParams:
    page: int | None = Query(None, description="Page number")
    limit: int | None = Query(None, description="Number of items per page")
    keyword: str | None = Query(None, description="Keyword to search by")
