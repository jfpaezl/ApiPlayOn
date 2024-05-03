from sqlalchemy.orm import Session
from app.db.episodes_model import Episode
from app.persistence.schemas.episode_schema import EpisodeBase, EpisodeCreate, EpisodeUpdate, EpisodeInDBBase, Episode

def getEpisodeById(db: Session, episode_id: int):
    return db.query(Episode).filter(Episode.id == episode_id).first()

def createEpisode(db: Session, episode: EpisodeCreate):
    new_episode = Episode(**episode.dict())
    db.add(new_episode)
    db.commit()
    db.refresh(new_episode)
    return new_episode

def updateEpisode(db: Session, episode_id: int, episode: EpisodeUpdate):
    episode_to_update = db.query(Episode).filter(Episode.id == episode_id).first()
    for key, value in episode.dict().items():
        if value is not None:
            setattr(episode_to_update, key, value)
    db.commit()
    db.refresh(episode_to_update)
    return episode_to_update

def deleteEpisode(db: Session, episode_id: int):
    episode_to_delete = db.query(Episode).filter(Episode.id == episode_id).first()
    db.delete(episode_to_delete)
    db.commit()
    return episode_to_delete

def getEpisodesBySeasonId(db: Session, season_id: int):
    return db.query(Episode).filter(Episode.season_id == season_id).all()