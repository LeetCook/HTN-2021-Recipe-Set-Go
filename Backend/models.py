from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)