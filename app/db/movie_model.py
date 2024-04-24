from sqlalchemy import Column, Integer, String, Text
from ..config.connection import Base

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(45), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    director = Column(String(45), nullable=False)
    trailer_url = Column(String(255), nullable=False)
    release_year = Column(Integer, nullable=False)
    recommended_age = Column(Integer, nullable=False)
    cover_image = Column(String(255), nullable=False)
    poster_image = Column(String(255), nullable=False)