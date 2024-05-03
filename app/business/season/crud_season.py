from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.persistence.schemas.season_schema import Season, SeasonUpdate
from app.config.connection import get_db
from app.persistence.crud.season_crud import createSeason, getSeasonById, getSeasonsBySeriesId, updateSeason, deleteSeason

def create_season(season: Season, db : Session = Depends(get_db)):
    try:
        return createSeason(db, season)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_season_by_id(season_id: int, db : Session = Depends(get_db)):
    try:
        season = getSeasonById(db, season_id)
        if season is None:
            raise HTTPException(status_code=404, detail="Season not found")
        return season
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_seasons_by_series_id(series_id: int, db : Session = Depends(get_db)):
    try:
        seasons = getSeasonsBySeriesId(db, series_id)
        if seasons is None:
            raise HTTPException(status_code=404, detail="Seasons not found")
        return seasons
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_season(season_id: int, season: SeasonUpdate, db : Session = Depends(get_db)):
    try:
        season_to_update = getSeasonById(db, season_id)
        if season_to_update is None:
            raise HTTPException(status_code=404, detail="Season not found")
        return updateSeason(db, season_id, season)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))    
    

