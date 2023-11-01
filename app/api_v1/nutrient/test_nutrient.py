import pytest

from ..config import settings


@pytest.mark.asyncio
# Create nutrient
async def test_nutrient_crud(test_client, mongo_client):
    response = test_client.post(
        "/nutrients/",
        json={
            "name": "Carbohydrate",
            "description": "Energy foods",
            "is_macro": True,
        },
    )

    assert response.status_code == 200
    data = response.json()['data']
    macro_nutrient_id = data['_id']

    # Create  Nutrient
    response = test_client.post(
        "/nutrients/",
        json={
            "name": "Carbohydrate",
            "description": "Energy foods",
            "macro_id": macro_nutrient_id,
            "is_macro": False
        },
    )

    assert response.status_code == 200
    data = response.json()['data']
    nutrient_id = data['_id']

    # Assert that the new  nutrient has the right macro nutrient ID
    assert data['macro_id'] == macro_nutrient_id

    response = test_client.get("/nutrients/"+nutrient_id)
    # Assert that we can fetch the created  nutrient
    assert response.status_code == 200
    assert response.json()['data'] == data

    response = test_client.get("/nutrients/")
    assert response.status_code == 200
    data = response.json()['data']
    assert len(data) == 1

    # Teardown
    mongo_client.drop_database(settings.mongodb_test_db_name)


@pytest.mark.asyncio
async def test_getnutrients_paginated(test_client, mongo_client):
    response = test_client.get("/nutrients")
    assert response.status_code == 200
    data = response.json()['data']
    assert len(data) == 0

    for i in range(20):
        response = test_client.post(
            "/nutrients/",
            json={
                "name": "Carbohydrate",
                "description": "Energy foods",
            },
        )

        assert response.status_code == 200

    response = test_client.post(
        "/nutrients/",
        json={
            "name": "Carbohydrate",
            "description": "Energy foods",
        },
    )

    assert response.status_code == 200

    response = test_client.get(
        "/nutrients?limit=3&page=1&keyword=Kaduna")
    assert response.status_code == 200
    data = response.json()['data']
    assert len(data) == 1

    response = test_client.get("/nutrients")
    assert response.status_code == 200
    data = response.json()['data']
    assert len(data) == 21

    # Teardown
    mongo_client.drop_database(settings.mongodb_test_db_name)
