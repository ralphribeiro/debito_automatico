from fastapi.testclient import TestClient

from app.core import config


def test_get_access_token(client: TestClient):
    login_data = {"username": config.FIRST_SUPERUSER,
                  "password": config.FIRST_SUPERUSER_PASSWORD}
    req = client.post(f"{config.API_V1_STR}/login/access-token",
                      data=login_data)
    tokens = req.json()
    assert req.status_code == 200
    assert "access_token" in tokens
