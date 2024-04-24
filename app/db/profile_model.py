from sqlalchemy import Column, Integer, String, ForeignKey
from ..config.connection import Base

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    image = Column(String(255))
    users_id = Column(Integer, ForeignKey('users.id'))