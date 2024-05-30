from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.config.connection import get_db
from app.persistence.crud.series_crud import getSeriesByCategoryId

def get_series_by_category(category_id: int, db: Session = Depends(get_db)):
    try:
        series = getSeriesByCategoryId(db, category_id)
        if not series:
            raise HTTPException(status_code=404, detail="No series found for the given category")
        return series
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))