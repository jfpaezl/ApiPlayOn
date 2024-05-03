from sqlalchemy.orm import Session
from app.db.seasons_model import Season
from app.persistence.schemas.season_schema import SeasonUpdate, Season

def getSeasonById(db: Session, season_id: int):
    return db.query(Season).filter(Season.id == season_id).first()

def createSeason(db: Session, season: Season):
    new_season = Season(**season.dict())
    db.add(new_season)
    db.commit()
    db.refresh(new_season)
    return new_season

def updateSeason(db: Session, season_id: int, season: SeasonUpdate):
    season_to_update = db.query(Season).filter(Season.id == season_id).first()
    for key, value in season.dict().items():
        if value is not None:
            setattr(season_to_update, key, value)
    db.commit()
    db.refresh(season_to_update)
    return season_to_update

def deleteSeason(db: Session, season_id: int):
    season_to_delete = db.query(Season).filter(Season.id == season_id).first()
    db.delete(season_to_delete)
    db.commit()
    return season_to_delete

def getSeasonsBySeriesId(db: Session, series_id: int):
    return db.query(Season).filter(Season.series_id == series_id).all()

def getSeasonsByReleaseYear(db: Session, release_year: int):
    return db.query(Season).filter(Season.release_year == release_year).all()

