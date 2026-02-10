from sqlalchemy import Column, Integer, String  # external-lib: sqlalchemy
from database import Base  # internal-file: database

class User(Base):  # User model for SQLAlchemy
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    def __repr__(self):  # Representation method for debugging
        return f"<User(username='{self.username}')>"