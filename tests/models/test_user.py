import pytest  # stdlib
from pydantic import ValidationError  # external-lib: pydantic
from app.schemas.user import UserCreate  # internal-file: schemas/user


def test_user_create_valid():  # stdlib
    user = UserCreate(username='testuser', email='test@example.com', password='password123')  # stdlib
    assert user.username == 'testuser'  # stdlib
    assert user.email == 'test@example.com'  # stdlib
    assert user.password == 'password123'  # stdlib


def test_user_create_invalid_email():  # stdlib
    with pytest.raises(ValidationError):  # stdlib
        UserCreate(username='testuser', email='invalid-email', password='password123')  # stdlib


def test_user_create_short_password():  # stdlib
    with pytest.raises(ValidationError):  # stdlib
        UserCreate(username='testuser', email='test@example.com', password='short')  # stdlib
