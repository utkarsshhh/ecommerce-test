from sqlalchemy import create_engine, MetaData  # external-lib: sqlalchemy
from sqlalchemy.orm import sessionmaker, declarative_base  # external-lib: sqlalchemy
from typing import Generator  # stdlib
import os  # stdlib

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # stdlib
# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)  # external-lib: sqlalchemy
# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # external-lib: sqlalchemy
# Create a Base class for declarative models
Base = declarative_base()  # external-lib: sqlalchemy

# Dependency to get DB session
def get_db() -> Generator:
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session to the caller
    finally:
        db.close()  # Ensure the session is closed after use

# This file handles the database connection for user authentication and other operations.