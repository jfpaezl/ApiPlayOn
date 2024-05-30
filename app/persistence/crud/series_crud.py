from sqlalchemy.orm import Session
from app.db.series_model import Series
from app.db.seriescategory_model import SeriesCategory
from app.db.category_model import Category
from app.persistence.schemas.series_schema import SeriesSchema, UpdateSeriesSchema

def getSeriesById(db: Session, series_id: int):
    return db.query(Series).filter(Series.id == series_id).first()

def createSeries(db: Session, series: SeriesSchema):
    new_series = Series(**series.dict())
    db.add(new_series)
    db.commit()
    db.refresh(new_series)
    return new_series

def updateSeries(db: Session, series_id: int, series: UpdateSeriesSchema):
    series_to_update = db.query(Series).filter(Series.id == series_id).first()
    for key, value in series.dict().items():
        if value is not None:
            setattr(series_to_update, key, value)
    db.commit()
    db.refresh(series_to_update)
    return series_to_update

def deleteSeries(db: Session, series_id: int):
    series_to_delete = db.query(Series).filter(Series.id == series_id).first()
    db.delete(series_to_delete)
    db.commit()
    return series_to_delete

def getSeriesByCategoryId(db: Session, category_id: int):
    series =  db.query(Series.id, Series.title, Series.cover_image, Series.is_active).join(SeriesCategory, Series.id == SeriesCategory.series_id)\
                        .join(Category, SeriesCategory.categorys_id == Category.id)\
                        .filter(Category.id == category_id).all()
    return [serie._asdict() for serie in series]