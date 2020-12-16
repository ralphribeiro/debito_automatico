from fastapi.testclient import TestClient

from app.core import config


def test_hello_world(client: TestClient):
    res = client.get(f"{config.API_V1_STR}/")
    data = res.json()
    assert data["message"] == "Hello world!"