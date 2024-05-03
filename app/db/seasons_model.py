from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..config.connection import Base

class Season(Base):
    __tablename__ = "seasons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    series_id = Column(Integer, ForeignKey("series.id"), nullable=False)
    season_number = Column(Integer, nullable=False)
    title = Column(String(255))
    description = Column(Text)
    release_date = Column(Date)

    series = relationship("Series", back_populates="seasons")
    episodes = relationship("Episode", back_populates="season")