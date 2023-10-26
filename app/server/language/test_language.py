import pytest
from ..database import client as db_client, db_name
from ..config import settings
from bson import ObjectId


@pytest.mark.asyncio
# Create Ethnicity
async def test_create_language(test_client):
    response = test_client.post(
        "/ethnicities/",
        json={
            "name": "Waffirians",
            "description": "People of Warri",
            "lga_id": str(ObjectId())
        },
    )

    assert response.status_code == 200
    data = response.json()['data']
    ethnicity_id = data['_id']

    # Create Language
    response = test_client.post(
        "/languages/",
        json={
            "name": "Urhobo",
            "description": "A major language in Delta State",
            "ethnicity_id": ethnicity_id
        },
    )

    assert response.status_code == 200
    data = response.json()['data']
    _id = data['_id']

    # Assert that the new language has the right ethnicity ID
    assert data['ethnicity_id'] == ethnicity_id

    response = test_client.get("/languages/"+_id)
    # Assert that we can fetch the created language
    assert response.status_code == 200
    assert response.json()['data'] == data

    response = test_client.get("/languages/")
    # Assert that we have the right number of languages
    assert response.status_code == 200
    data = response.json()['data']
    assert len(data) == 1


# @pytest.mark.asyncio
# async def test_get_languages(test_client):
#     response = test_client.get("/languages")
#     response = test_client.post(
#         "/languages/",
#         json={
#             "name": "Urhobo",
#             "description": "A major language in Delta State"
#         },
#     )

#     data: list = response.json()['data']
#     print(data)

#     assert response.status_code == 200
#     assert len(data) == 1
