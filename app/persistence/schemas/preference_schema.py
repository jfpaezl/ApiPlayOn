from pydantic import BaseModel, Field
from typing import Optional

class PreferenceSchema(BaseModel):
    rating: Optional[int] = None
    like: Optional[bool] = False
    playlist: Optional[bool] = False
    profiles_id: int = Field(...)
    series_id: Optional[int] = None
    movies_id: Optional[int] = None

class UpdatePreferenceSchema(BaseModel):
    rating: Optional[int] = None
    like: Optional[bool] = None
    playlist: Optional[bool] = None
    profiles_id: Optional[int] = None
    series_id: Optional[int] = None
    movies_id: Optional[int] = None