import pytest

from ..config import settings


@pytest.mark.asyncio
# Create macro nutrient
async def test_micro_nutrient_crud(test_client, mongo_client):
    response = test_client.post(
        "/macro_nutrients/",
        json={
            "name": "Carbohydrate",
            "description": "Energy foods",
        },
    )

    assert response.status_code == 200
    data = response.json()['data']
    macro_nutrient_id = data['_id']

    # Create Micro Nutrient
    response = test_client.post(
        "/micro_nutrients/",
        json={
            "name": "Carbohydrate",
            "description": "Energy foods",
            "macro_nutrient_id": macro_nutrient_id
        },
    )

    assert response.status_code == 200
    data = response.json()['data']
    micro_nutrient_id = data['_id']

    # Assert that the new micro nutrient has the right macro nutrient ID
    assert data['macro_nutrient_id'] == macro_nutrient_id

    response = test_client.get("/micro_nutrients/"+micro_nutrient_id)
    # Assert that we can fetch the created micro nutrient
    assert response.status_code == 200
    assert response.json()['data'] == data

    response = test_client.get("/micro_nutrients/")
    assert response.status_code == 200
    data = response.json()['data']
    assert len(data) == 1

    # Teardown
    mongo_client.drop_database(settings.mongodb_test_db_name)


@pytest.mark.asyncio
async def test_get_micro_nutrients_paginated(test_client, mongo_client):
    response = test_client.get("/micro_nutrients")
    assert response.status_code == 200
    data = response.json()['data']
    assert len(data) == 0

    for i in range(20):
        response = test_client.post(
            "/micro_nutrients/",
            json={
                "name": "Carbohydrate",
                "description": "Energy foods",
                "macro_nutrient_id": '65392b337c2ebd6d003ddb4a'
            },
        )

        assert response.status_code == 200

    response = test_client.post(
        "/micro_nutrients/",
        json={
            "name": "Carbohydrate",
            "description": "Energy foods",
            "macro_nutrient_id": '65392b337c2ebd6d003ddb4a'
        },
    )

    assert response.status_code == 200

    response = test_client.get(
        "/micro_nutrients?limit=3&page=1&keyword=Kaduna")
    assert response.status_code == 200
    data = response.json()['data']
    assert len(data) == 1

    response = test_client.get("/micro_nutrients")
    assert response.status_code == 200
    data = response.json()['data']
    assert len(data) == 21

    # Teardown
    mongo_client.drop_database(settings.mongodb_test_db_name)
