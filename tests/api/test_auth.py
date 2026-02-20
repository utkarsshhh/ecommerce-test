import pytest  # stdlib
from fastapi.testclient import TestClient  # external-lib: fastapi
from app.main import app  # internal-file: main

@pytest.fixture  # stdlib
def client():  # stdlib
    client = TestClient(app)  # external-lib: fastapi
    return client

@pytest.fixture  # stdlib
def create_user(client):  # stdlib
    # Create a user for testing
    response = client.post("/token", data={  # internal-file: main
        "username": "testuser",  # stdlib
        "password": "testpassword"  # stdlib
    })
    assert response.status_code == 200  # stdlib


def test_login_valid(client, create_user):  # stdlib
    response = client.post("/token", data={  # internal-file: main
        "username": "testuser",  # stdlib
        "password": "testpassword"  # stdlib
    })
    assert response.status_code == 200  # stdlib
    assert "access_token" in response.json()  # stdlib


def test_login_invalid_username(client):  # stdlib
    response = client.post("/token", data={  # internal-file: main
        "username": "invaliduser",  # stdlib
        "password": "testpassword"  # stdlib
    })
    assert response.status_code == 400  # stdlib
    assert "detail" in response.json()  # stdlib


def test_login_invalid_password(client, create_user):  # stdlib
    response = client.post("/token", data={  # internal-file: main
        "username": "testuser",  # stdlib
        "password": "wrongpassword"  # stdlib
    })
    assert response.status_code == 400  # stdlib
    assert "detail" in response.json()  # stdlib


def test_login_no_credentials(client):  # stdlib
    response = client.post("/token", data={})  # internal-file: main
    assert response.status_code == 422  # stdlib
    assert "detail" in response.json()  # stdlib