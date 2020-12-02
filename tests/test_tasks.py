import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def user_data(temp_db):
    with TestClient(app) as client:
        client.post(
            "/users/register",
            json={
                "email": "namer@example.com",
                "password": "Passworderrr",
                "name": "TestName1"
            }
        )

        data = {
            "grant_type": None,
            "username": "namer@example.com",
            "password": "Passworderrr",
            "scopes": [],
            "client_id": None,
            "client_secret": None,
        }

        response = client.post(
            "users/login",
            data=data
        )

    return response.json()


@pytest.fixture
def create_task(user_data):
    data = {
        "title": "taaask",
        "text": "teeeext",
        "completity_date": "2020-12-01",
        "is_completed": False
    }

    with TestClient(app) as client:
        response = client.post(
            "/tasks/",
            headers={"Authorization": f"Bearer {user_data['access_token']}"},
            json=data
        )

    return response


@pytest.mark.run(order=1)
def test_create_task(temp_db, create_task):
    assert create_task.status_code == 201


@pytest.mark.run(order=2)
def test_get_task_list(temp_db, user_data):
    with TestClient(app) as client:
        response = client.get(
            "/tasks",
            headers={"Authorization": f"Bearer {user_data['access_token']}"}
        )

    assert response.status_code == 200


@pytest.mark.run(order=3)
def test_get_task_single(temp_db, user_data, create_task):
    with TestClient(app) as client:
        response = client.get(
            f"/tasks/{create_task.json()['id']}",
            headers={"Authorization": f"Bearer {user_data['access_token']}"}
        )
    
    assert response.status_code == 200


@pytest.mark.run(order=4)
def test_task_completed(temp_db, user_data, create_task):
    with TestClient(app) as client:
        response = client.patch(
            f"/tasks/completed/{create_task.json()['id']}",
            headers={"Authorization": f"Bearer {user_data['access_token']}"}
        )

    assert response.status_code == 200


@pytest.mark.run(order=5)
def test_delete_task(temp_db, user_data, create_task):
    with TestClient(app) as client:
        response = client.delete(
            f"/tasks/{create_task.json()['id']}",
            headers={"Authorization": f"Bearer {user_data['access_token']}"}
        )

    assert response.status_code == 204


