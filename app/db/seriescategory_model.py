from sqlalchemy import Column, Integer, ForeignKey
from ..config.connection import Base

class SeriesCategory(Base):
    __tablename__ = 'series_has_categorys'

    series_id = Column(Integer, ForeignKey('series.id'), primary_key=True)
    categorys_id = Column(Integer, ForeignKey('categorys.id'), primary_key=True)
