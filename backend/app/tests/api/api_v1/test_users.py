from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core import config
from app.schemas.user import UserCreate
from app.tests.utils.utils import random_email, random_lower_string


def test_get_superuser_me(client: TestClient,
                          superuser_token_headers: Dict[str, str]):
    for _ in range(10):
        res = client.get(f"{config.API_V1_STR}/users/me",
                        headers=superuser_token_headers)
        current_user = res.json()
        assert current_user
        assert current_user["is_active"] is True
        assert current_user["is_superuser"] is True


def test_get_normal_user_me(client: TestClient,
                            normal_user_token_headers: Dict[str, str]):
    res = client.get(f"{config.API_V1_STR}/users/me",
                     headers=normal_user_token_headers)
    current_user = res.json()
    assert current_user
    assert current_user["is_active"] is True
    assert current_user["is_superuser"] is False


def test_get_existing_user(client: TestClient,
                           superuser_token_headers: dict, db: Session):
    username = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=username, password=password)
    user = crud.user.create(db, obj_in=user_in)
    user_id = user.id
    res = client.get(f"{config.API_V1_STR}/users/{user_id}",
                     headers=superuser_token_headers)

    assert 200 <= res.status_code < 300

    api_user = res.json()
    existing_user = crud.user.get_by_email(db, email=username)

    assert existing_user
    assert existing_user.email == api_user["email"]


def test_retrieve_users(db: Session, client: TestClient,
                        superuser_token_headers: dict):
    username = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=username, password=password)
    crud.user.create(db, obj_in=user_in)

    username2 = random_email()
    password2 = random_lower_string()
    user_in2 = UserCreate(email=username2, password=password2)
    crud.user.create(db, obj_in=user_in2)

    res = client.get(f"{config.API_V1_STR}/users/",
                     headers=superuser_token_headers)

    all_users = res.json()

    assert len(all_users) > 1
    for item in all_users:
        assert "email" in item


def test_create_user_new_email(client: TestClient,
                               superuser_token_headers: dict,
                               db: Session):
    username = random_email()
    password = random_lower_string()
    data = {"email": username, "password": password}
    res = client.post(f"{config.API_V1_STR}/users/",
                      headers=superuser_token_headers, json=data)

    assert 200 <= res.status_code < 300

    created_user = res.json()
    user = crud.user.get_by_email(db, email=username)

    assert user
    assert user.email == created_user["email"]
