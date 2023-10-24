from fastapi import FastAPI
from fastapi.testclient import TestClient
from server.app import app

client = TestClient(app)


def test_read_states():
    response = client.get("/states/")
    assert response.status_code == 200
    assert response.json() == []
