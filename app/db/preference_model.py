from sqlalchemy import Column, Integer, Boolean, ForeignKey
from ..config.connection import Base

class Preference(Base):
    __tablename__ = 'preferences'

    id = Column(Integer, primary_key=True, autoincrement=True)
    rating = Column(Integer)
    like = Column(Boolean)
    playlist = Column(Boolean)
    profiles_id = Column(Integer, ForeignKey('profiles.id'))
    series_id = Column(Integer, ForeignKey('series.id'))
    movies_id = Column(Integer, ForeignKey('movies.id'))