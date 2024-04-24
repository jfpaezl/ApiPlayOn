from sqlalchemy import Column, Integer, String
from ..config.connection import Base

class Category(Base):
    __tablename__ = 'categorys'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)