
from dataclasses import dataclass
from fastapi import Query


def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}


@dataclass
class ListQueryParams:
    page: int | None = Query(None, description="Page number")
    limit: int | None = Query(None, description="Number of items per page")
    keyword: str | None = Query(None, description="Keyword to search by")
