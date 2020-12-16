from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core import config
from app.tests.utils.debit import create_debit_request


"""
    Autenticação e acesso a plataforma

Um usuário autenticado,

    solicita uma ativação de débito automático
    cancela uma solicitação de ativação
    aprova uma solicitação de ativação
    rejeita uma solicitação de ativação
    visualiza uma solicitação
"""


def test_request_automatic_debit(client: TestClient,
                                 normal_random_user_token_headers: Dict[str, str],
                                 db: Session):
    res = client.get(f"{config.API_V1_STR}/debits/request",
                     headers=normal_random_user_token_headers)
    assert res.status_code == 200
