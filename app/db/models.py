# Database models for SQLAlchemy

from sqlalchemy import Column, Integer, String, Boolean  # external-lib: sqlalchemy
from .session import Base  # internal-file: session


class User(Base):  # stdlib
    __tablename__ = 'users'  # stdlib

    id = Column(Integer, primary_key=True, index=True)  # stdlib
    username = Column(String(50), unique=True, index=True, nullable=False)  # stdlib
    email = Column(String(100), unique=True, index=True, nullable=False)  # stdlib
    hashed_password = Column(String(128), nullable=False)  # stdlib
    is_active = Column(Boolean, default=True)  # stdlib

    def __repr__(self):  # stdlib
        return f'<User id={self.id} username={self.username}>'  # stdlib
