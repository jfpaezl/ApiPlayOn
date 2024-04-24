from pydantic import BaseModel, Field
from typing import Optional

class ProfileSchema(BaseModel):
    name: str = Field(...)
    image: Optional[str] = Field(None)
    users_id: int = Field(...)

class UpdateProfileSchema(BaseModel):
    name: Optional[str] = None
    image: Optional[str] = None
    users_id: Optional[int] = None