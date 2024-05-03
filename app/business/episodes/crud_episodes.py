from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.persistence.schemas.episode_schema import EpisodeBase, EpisodeCreate, EpisodeUpdate, EpisodeInDBBase, Episode
from app.config.connection import get_db
from app.persistence.crud.episode_crud import getEpisodeById, createEpisode, updateEpisode, deleteEpisode, getEpisodesBySeasonId

def create_episode(episode: EpisodeCreate, db: Session = Depends(get_db)):
    try:
        return createEpisode(db, episode)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_episode_by_id(episode_id: int, db: Session = Depends(get_db)):
    try:
        episode = getEpisodeById(db, episode_id)
        if episode is None:
            raise HTTPException(status_code=404, detail="Episode not found")
        return episode
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_episodes_by_season_id(season_id: int, db: Session = Depends(get_db)):
    try:
        episodes = getEpisodesBySeasonId(db, season_id)
        if episodes is None:
            raise HTTPException(status_code=404, detail="Episodes not found")
        return episodes
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_episode(episode_id: int, episode: EpisodeUpdate, db: Session = Depends(get_db)):
    try:
        episode_to_update = getEpisodeById(db, episode_id)
        if episode_to_update is None:
            raise HTTPException(status_code=404, detail="Episode not found")
        return updateEpisode(db, episode_id, episode)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    