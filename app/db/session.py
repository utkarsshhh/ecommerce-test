# Database session management for FastAPI using SQLAlchemy

from sqlalchemy import create_engine  # external-lib: sqlalchemy
from sqlalchemy.ext.declarative import declarative_base  # external-lib: sqlalchemy
from sqlalchemy.orm import sessionmaker  # external-lib: sqlalchemy

# Database URL (update with your database configuration)
DATABASE_URL = "sqlite:///./test.db"  # stdlib

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # external-lib: sqlalchemy

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # external-lib: sqlalchemy

# Create a declarative base
Base = declarative_base()  # external-lib: sqlalchemy

# Dependency to get the database session

def get_db():  # stdlib
    db = SessionLocal()  # stdlib
    try:
        yield db  # stdlib
    finally:
        db.close()  # stdlib
