from sqlalchemy import Column, Integer, String  # external-lib: sqlalchemy
from app.db.session import Base  # internal-file: db/session

class User(Base):  # User model for the database
    __tablename__ = 'users'  # Define the table name

    id = Column(Integer, primary_key=True, index=True)  # User ID
    username = Column(String, unique=True, index=True)  # Unique username
    email = Column(String, unique=True, index=True)  # Unique email address
    hashed_password = Column(String)  # Hashed password

    def __repr__(self):  # Represent the User object
        return f'<User id={self.id} username={self.username}>'  # String representation of the user
