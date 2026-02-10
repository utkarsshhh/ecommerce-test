# Authentication Service for User Login

from passlib.context import CryptContext  # external-lib: passlib
from sqlalchemy.orm import Session  # external-lib: sqlalchemy
from models import User  # internal-file: models
from fastapi import HTTPException, status  # external-lib: fastapi

# Create a CryptContext to hash and verify passwords
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class AuthenticationService:
    """
    Service class to handle user authentication logic.
    """

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify the provided password against the hashed password."""
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def authenticate_user(db: Session, username: str, password: str) -> User:
        """Authenticate a user by checking their credentials."""
        user = db.query(User).filter(User.username == username).first()
        if not user or not AuthenticationService.verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user
