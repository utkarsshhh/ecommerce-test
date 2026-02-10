import pytest  # external-lib: pytest
from fastapi.testclient import TestClient  # external-lib: fastapi
from main import app  # internal-file: main

# Test cases for the login functionality
@pytest.fixture(scope='module')
def test_client():
    """Fixture to create a test client for FastAPI app."""
    client = TestClient(app)
    yield client


def test_login_success(test_client):
    """Test successful login with valid credentials."""
    response = test_client.post('/login', json={'username': 'valid_user', 'password': 'valid_pass'})
    assert response.status_code == 200
    assert response.json() == {'message': 'Login successful'}


def test_login_invalid_credentials(test_client):
    """Test login with invalid credentials."""
    response = test_client.post('/login', json={'username': 'invalid_user', 'password': 'invalid_pass'})
    assert response.status_code == 401
    assert response.json() == {'detail': 'Invalid credentials'}


def test_login_missing_fields(test_client):
    """Test login with missing fields in request."""
    response = test_client.post('/login', json={'username': 'valid_user'})  # missing password
    assert response.status_code == 422
    assert 'detail' in response.json()

    response = test_client.post('/login', json={'password': 'valid_pass'})  # missing username
    assert response.status_code == 422
    assert 'detail' in response.json()