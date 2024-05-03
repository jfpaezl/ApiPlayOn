from pydantic import BaseModel

class SeriesCategorySchema(BaseModel):
    series_id: int
    category_id: int

    class Config:
        orm_mode = True