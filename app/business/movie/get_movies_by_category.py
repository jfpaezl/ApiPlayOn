from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.config.connection import get_db
from app.persistence.crud.movie_crud import getMoviesByCategoryId, getMoviesByCategoryName

def get_movies_by_category(category_id: int, db: Session = Depends(get_db)):
    try:
        movies = getMoviesByCategoryId(db, category_id)
        if not movies:
            raise HTTPException(status_code=404, detail="No movies found for the given category")
        return movies
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_movies_by_category_name(category_name: str, db: Session = Depends(get_db)):
    try:
        movies = getMoviesByCategoryName(db, category_name)
        if not movies:
            raise HTTPException(status_code=404, detail="No movies found for the given category")
        return movies
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

