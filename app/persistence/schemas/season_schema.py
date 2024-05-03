from pydantic import BaseModel
from typing import Optional
from datetime import date

# Esquema para Temporada
class SeasonBase(BaseModel):
    season_number: int
    title: Optional[str] = None
    description: Optional[str] = None
    release_date: Optional[date] = None


class SeasonUpdate(SeasonBase):
    pass

class SeasonInDBBase(SeasonBase):
    id: int
    series_id: int

    class Config:
        orm_mode = True

class Season(SeasonInDBBase):
    pass