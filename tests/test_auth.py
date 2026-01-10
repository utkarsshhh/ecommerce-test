import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy.orm import Session
from app.database import get_db

@pytest.fixture()
def client() -> TestClient:
    with TestClient(app) as c:
        yield c

@pytest.fixture()
def db_session() -> Session:
    db = next(get_db())
    yield db
    db.close()

def test_signup_success(client: TestClient, db_session: Session):
    response = client.post("/api/auth/signup", json={
        "name": "testuser",
        "password": "testpassword",
        "email": "testuser@example.com"
    })
    assert response.status_code == 201
    assert response.json() == {"msg": "User created successfully", "user_id": response.json()["user_id"]}

def test_signup_email_taken(client: TestClient, db_session: Session):
    db_session.execute("INSERT INTO users (name, email, hashed_password) VALUES ('testuser', 'testuser@example.com', 'hashed_password')")
    response = client.post("/api/auth/signup", json={
        "name": "newuser",
        "password": "testpassword",
        "email": "testuser@example.com"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}

def test_signup_invalid_email(client: TestClient, db_session: Session):
    response = client.post("/api/auth/signup", json={
        "name": "newuser",
        "password": "testpassword",
        "email": "invalid_email"
    })
    assert response.status_code == 422

def test_signup_short_password(client: TestClient, db_session: Session):
    response = client.post("/api/auth/signup", json={
        "name": "anotheruser",
        "password": "short",
        "email": "anotheruser@example.com"
    })
    assert response.status_code == 422

def test_signup_missing_fields(client: TestClient, db_session: Session):
    response = client.post("/api/auth/signup", json={
        "name": "",
        "password": "",
        "email": ""
    })
    assert response.status_code == 422
