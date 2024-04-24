from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.persistence.schemas.series_schema import SeriesSchema, UpdateSeriesSchema
from app.config.connection import get_db
from app.persistence.crud.series_crud import createSeries, getSeriesById, updateSeries, deleteSeries

def create_series(series: SeriesSchema, db : Session = Depends(get_db)):
    try:
        return createSeries(db, series)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def get_series_by_id(series_id: int, db : Session = Depends(get_db)):
    try:
        series = getSeriesById(db, series_id)
        if series is None:
            raise HTTPException(status_code=404, detail="Series not found")
        return series
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_series(series_id: int, series: UpdateSeriesSchema, db : Session = Depends(get_db)):
    try:
        series_to_update = getSeriesById(db, series_id)
        if series_to_update is None:
            raise HTTPException(status_code=404, detail="Series not found")
        return updateSeries(db, series_id, series)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_series(series_id: int, db : Session = Depends(get_db)):
    try:
        series = getSeriesById(db, series_id)
        if series is None:
            raise HTTPException(status_code=404, detail="Series not found")
        return deleteSeries(db, series_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    