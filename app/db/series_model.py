from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from ..config.connection import Base

class Series(Base):
    __tablename__ = 'series'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(45), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    director = Column(String(45), nullable=False)
    trailer_url = Column(String(255), nullable=False)
    release_year = Column(Integer, nullable=False)
    recommended_age = Column(Integer, nullable=False)
    cover_image = Column(String(255), nullable=False)
    poster_image = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    seasons = relationship("Season", back_populates="series")