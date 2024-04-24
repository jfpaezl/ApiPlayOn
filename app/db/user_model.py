from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from ..config.connection import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    token = Column(String(255))
    confirm = Column(Boolean)
    createdAt = Column(DateTime, default=datetime.now, nullable=False)
    updatedAt = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)