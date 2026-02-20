from fastapi import APIRouter, HTTPException, Depends  # external-lib: fastapi
from fastapi.security import OAuth2PasswordRequestForm  # external-lib: fastapi
from app.models.user import User  # internal-file: models/user
from app.schemas.user import UserOut  # internal-file: schemas/user
from app.services.auth import create_access_token, verify_password, get_current_user  # internal-file: services/auth

router = APIRouter()

# Dummy database simulation for demonstration purposes
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$KIXQZ9Yt5F9e3s5VxZt3.OTiH7q6J0g3UO3k8R7kz1eZs1PZC5eG2",  # bcrypt hashed 'secret'
    }
}

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):  # type: ignore
    """Login endpoint to authenticate user and return JWT token."""
    user = fake_users_db.get(form.username)
    if not user or not verify_password(form.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", response_model=UserOut)
async def read_users_me(current_user: User = Depends(get_current_user)):
    """Retrieve current user information."""
    return current_user
