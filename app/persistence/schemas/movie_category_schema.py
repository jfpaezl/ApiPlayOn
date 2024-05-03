from pydantic import BaseModel

class MovieCategorySchema(BaseModel):
    movies_id: int
    categorys_id: int

    class Config:
        orm_mode = True