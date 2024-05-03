from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.persistence.schemas.series_schema import SeriesCategorySchema
from app.config.connection import get_db
from app.persistence.crud.series_crud import createSeries
from app.persistence.crud.series_category_crud import createMultipleSeriesCategories

def create_serie(serie: SeriesCategorySchema, db: Session = Depends(get_db)):
    categories = serie.categories
    try:
        created_serie = createSeries(db, serie)
        if created_serie:
            createMultipleSeriesCategories(db, created_serie.id ,categories)
            return {"message": "Serie created successfully"}
        else:
            raise HTTPException(status_code=400, detail="Serie creation failed")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))