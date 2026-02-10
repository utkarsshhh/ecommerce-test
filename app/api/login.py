# Login API Endpoint

from fastapi import APIRouter, Depends, HTTPException, status  # external-lib: fastapi
from sqlalchemy.orm import Session  # external-lib: sqlalchemy
from database import get_db  # internal-file: database
from services.authentication import AuthenticationService  # internal-file: services/authentication
from models import User  # internal-file: models
from pydantic import BaseModel  # external-lib: pydantic

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login", response_model=User)  # API endpoint for user login
async def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    """Endpoint to log in a user with username and password."""
    user = AuthenticationService.authenticate_user(db, login_request.username, login_request.password)
    return user
