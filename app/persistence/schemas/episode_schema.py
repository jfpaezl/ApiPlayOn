from pydantic import BaseModel
from typing import Optional
from datetime import date

# Esquema para Capítulo
class EpisodeBase(BaseModel):
    episode_number: int
    title: str
    description: Optional[str] = None
    duration: Optional[int] = None
    release_date: Optional[date] = None

class EpisodeCreate(EpisodeBase):
    season_id: int

class EpisodeUpdate(EpisodeBase):
    pass

class EpisodeInDBBase(EpisodeBase):
    id: int
    season_id: int

    class Config:
        orm_mode = True

class Episode(EpisodeInDBBase):
    pass