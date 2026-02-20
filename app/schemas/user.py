from pydantic import BaseModel, EmailStr, constr  # external-lib: pydantic

class UserCreate(BaseModel):  # Pydantic schema for user creation
    username: constr(min_length=3, max_length=50)  # Username with length validation
    email: EmailStr  # Email address for the user
    password: constr(min_length=6)  # Password with minimum length validation

    class Config:  # Configuration for Pydantic model
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models

class UserOut(BaseModel):  # Pydantic schema for user output
    id: int  # User ID
    username: str  # Username for the user
    email: EmailStr  # Email address for the user

    class Config:  # Configuration for Pydantic model
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models
