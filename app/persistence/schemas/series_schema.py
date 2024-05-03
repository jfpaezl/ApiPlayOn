from pydantic import BaseModel, Field   
from typing import Optional

class SeriesSchema(BaseModel):
    title: str = Field(...)
    description: str
    director: str
    trailer_url: str
    release_year: int
    recommended_age: int
    cover_image: str
    poster_image: str
    is_active: bool = True

class UpdateSeriesSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    director: Optional[str] = None
    trailer_url: Optional[str] = None
    release_year: Optional[int] = None
    recommended_age: Optional[int] = None
    cover_image: Optional[str] = None
    poster_image: Optional[str] = None
    is_active: Optional[bool] = None

class SeriesCategorySchema(SeriesSchema):
    categories: list[int]