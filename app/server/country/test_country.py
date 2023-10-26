from fastapi.testclient import TestClient
import pytest


@pytest.mark.asyncio
async def test_create_country(test_client):
    response = test_client.post(
        "/countries/",
        json={
            "name": "Nigeria",
            "description": "The most populous nation in Africa"
        },
    )
    data = response.json()['data']
    _id = data['_id']
    assert response.status_code == 200

    response = test_client.get("/countries/"+_id)
    assert response.status_code == 200
    assert response.json()['data'] == data


@pytest.mark.asyncio
async def test_get_countries(test_client):
    response = test_client.get("/countries")
    assert response.status_code == 200
