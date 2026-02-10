from pydantic import BaseModel, EmailStr, Field  # external-lib: pydantic


class UserLogin(BaseModel):  # Define a Pydantic model for user login
    username: str = Field(..., description="Username or email of the user")  # Required field for username or email
    password: str = Field(..., min_length=6, description="Password of the user")  # Required field for password with minimum length

    class Config:  # Configuration for the Pydantic model
        schema_extra = {  # Example of how the model can be used
            "example": {  # Example data
                "username": "user@example.com",
                "password": "securepassword"
            }
        }