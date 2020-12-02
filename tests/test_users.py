import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.mark.run(order=1)
def test_register_user(temp_db):

    with TestClient(app) as client:
        response = client.post(
            "/users/register",
            json={
                "email": "koricza@example.com",
                "password": "stringify123",
                "name": "TestName"
            }
        )

    assert response.status_code == 201


@pytest.mark.run(order=2)
def test_login_user(temp_db):

    data = {
        "grant_type": None,
        "username": "koricza@example.com",
        "password": "stringify123",
        "scopes": [],
        "client_id": None,
        "client_secret": None,
    }

    with TestClient(app) as client:
        response = client.post(
            "users/login",
            data=data
        )

    assert response.status_code == 200