from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from ..common.schema import ListQueryParams
from ..common.services import retrieve_list
from ..database import state_collection
from .state_helper import deserialize_state

from .state_service import (
    add_state,
    delete_state,
    retrieve_state,
    update_state,
)

from .state_schema import (
    CreateStateDto,
    UpdateStateDto,
)


from ..common.schema import ResponseModel, ErrorResponseModel

router = APIRouter()


@router.post("/", response_description="State data added into the database")
async def add_state_data(state: CreateStateDto = Body(...)):
    state = jsonable_encoder(state)
    new_state = await add_state(state)
    return ResponseModel(new_state, "state added successfully.")


@router.get("/", response_description="States retrieved")
async def get_states(params: ListQueryParams = Depends()):
    states = await retrieve_list(params=params, collection=state_collection, deserialize=deserialize_state)

    if states:
        return ResponseModel(states, "States data retrieved successfully")

    return ResponseModel(states, "Empty list returned")


@router.get("/{id}", response_description="state data retrieved")
async def get_state_data(id):
    state = await retrieve_state(id)

    if state:
        return ResponseModel(state, "state data retrieved successfully")

    return ErrorResponseModel("An error occurred.", 404, "state doesn't exist.")


@router.put("/{id}")
async def update_state_data(id: str, req: UpdateStateDto = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_state = await update_state(id, req)

    if updated_state:
        return ResponseModel(
            "state with ID: {} name update is successful".format(id),
            "state name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", response_description="state data deleted from the database")
async def delete_state_data(id: str):
    deleted_state = await delete_state(id)
    if deleted_state:
        return ResponseModel(
            "state with ID: {} removed".format(
                id), "state deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "state with id {0} doesn't exist".format(
            id)
    )
