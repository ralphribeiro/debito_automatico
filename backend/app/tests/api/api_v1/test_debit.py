from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core import config
from app.tests.utils.debit import create_debit_request


"""
    [x] - Autenticação e acesso a plataforma

Um usuário autenticado,

    [x] - solicita uma ativação de débito automático
    [x] - cancela uma solicitação de ativação (super user)
    [x] - aprova uma solicitação de ativação (super user)
    [x] - rejeita uma solicitação de ativação (super user)
    [x] - visualiza uma solicitação
"""


def test_request_automatic_debit(client: TestClient,
                                 normal_random_user_token_headers: dict,
                                 db: Session):
    res = client.get(f"{config.API_V1_STR}/debits/request",
                     headers=normal_random_user_token_headers)
    assert res.status_code == 200


def test_cancel_request_automatic_debit_with_super_user(
    client: TestClient,
    superuser_token_headers: dict,
    db: Session
):
    status_in = "canceled"
    debit = create_debit_request(db)
    res = client.put(
        f"{config.API_V1_STR}/debits/{debit.id}?status={status_in}",
        headers=superuser_token_headers
    )
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == status_in


def test_cancel_request_automatic_debit_with_normal_user(
    client: TestClient,
    normal_user_token_headers: dict,
    db: Session
):
    status_in = "canceled"
    debit = create_debit_request(db)
    res = client.put(
        f"{config.API_V1_STR}/debits/{debit.id}?status={status_in}",
        headers=normal_user_token_headers
    )
    assert res.status_code == 400


def test_approve_request_automatic_debit_with_super_user(
    client: TestClient,
    superuser_token_headers: dict,
    db: Session
):
    status_in = "approved"
    debit = create_debit_request(db)
    res = client.put(
        f"{config.API_V1_STR}/debits/{debit.id}?status={status_in}",
        headers=superuser_token_headers
    )
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == status_in


def test_approve_request_automatic_debit_with_normal_user(
    client: TestClient,
    normal_user_token_headers: dict,
    db: Session
):
    status_in = "canceled"
    debit = create_debit_request(db)
    res = client.put(
        f"{config.API_V1_STR}/debits/{debit.id}?status={status_in}",
        headers=normal_user_token_headers
    )
    assert res.status_code == 400


def test_reject_request_automatic_debit_with_super_user(
    client: TestClient,
    superuser_token_headers: dict,
    db: Session
):
    status_in = "rejected"
    debit = create_debit_request(db)
    res = client.put(
        f"{config.API_V1_STR}/debits/{debit.id}?status={status_in}",
        headers=superuser_token_headers
    )
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == status_in


def test_reject_request_automatic_debit_with_normal_user(
    client: TestClient,
    normal_user_token_headers: dict,
    db: Session
):
    status_in = "rejected"
    debit = create_debit_request(db)
    res = client.put(
        f"{config.API_V1_STR}/debits/{debit.id}?status={status_in}",
        headers=normal_user_token_headers
    )
    assert res.status_code == 400


def test_invalid_status_request_automatic_debit_with_super_user(
    client: TestClient,
    superuser_token_headers: dict,
    db: Session
):
    status_in = "papibaquigrafo"
    debit = create_debit_request(db)
    res = client.put(
        f"{config.API_V1_STR}/debits/{debit.id}?status={status_in}",
        headers=superuser_token_headers
    )
    assert res.status_code == 422


def test_get_request_automatic_debit(
    client: TestClient,
    normal_random_user_token_headers: dict,
    superuser_token_headers: dict,
    db: Session
):
    res = client.get(f"{config.API_V1_STR}/debits/request",
                     headers=normal_random_user_token_headers)
    assert res.status_code == 200

    data = res.json()
    status_in = "approved"
    res2 = client.put(
        f"{config.API_V1_STR}/debits/{data['id']}?status={status_in}",
        headers=superuser_token_headers
    )
    assert res2.status_code == 200
    data2 = res2.json()
    assert data2["status"] == status_in

    res3 = client.get(f"{config.API_V1_STR}/debits/{data2['owner_id']}",
                      headers=normal_random_user_token_headers)

    assert res3.status_code == 200
    data3 = res3.json()
    assert data2["id"] == data3["id"]
