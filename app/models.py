from sqlalchemy import Column, Integer, String  # external-lib: sqlalchemy
from database import Base  # internal-file: database

class User(Base):  # SQLAlchemy User model
    __tablename__ = 'users'  # Table name

    id = Column(Integer, primary_key=True, index=True)  # Primary key
    email = Column(String, unique=True, index=True)  # Unique email field
    hashed_password = Column(String)  # Hashed password field

    def __repr__(self):  # String representation of the User model
        return f'<User(id={self.id}, email={self.email})>'