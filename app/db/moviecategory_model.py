from sqlalchemy import Column, Integer, ForeignKey
from ..config.connection import Base

class MovieCategory(Base):
    __tablename__ = 'movies_has_categorys'

    movies_id = Column(Integer, ForeignKey('movies.id'), primary_key=True)
    categorys_id = Column(Integer, ForeignKey('categorys.id'), primary_key=True)
