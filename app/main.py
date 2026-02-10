from fastapi import FastAPI, Depends  # external-lib: fastapi
from fastapi.middleware.cors import CORSMiddleware  # external-lib: fastapi
from database import get_db  # internal-file: database
from sqlalchemy.orm import Session  # external-lib: sqlalchemy

app = FastAPI()  # Create FastAPI instance

# Allow CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this in production to restrict origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)  

@app.get("/")  # Root endpoint
async def root():  # Define root path
    return {"message": "Welcome to the User Authentication API!"}  # Response message

# Include any additional routes or endpoints here

# Dependency injection for using the database session

# This file initializes the FastAPI application and sets up the CORS middleware.