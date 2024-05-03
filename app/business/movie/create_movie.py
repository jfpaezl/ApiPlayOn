from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.persistence.schemas.movie_schema import MovieCategoriaSchema
from app.config.connection import get_db
from app.persistence.crud.movie_crud import createMovie
from app.persistence.crud.movie_category_crud import createMultipleMovieCategories

def create_movie(movie: MovieCategoriaSchema, db: Session = Depends(get_db)):
    categorias = movie.categories
    try:
        created_movie = createMovie(db, movie)
        if created_movie:
            createMultipleMovieCategories(db, created_movie.id ,categorias)
        else:
            raise HTTPException(status_code=400, detail="Movie creation failed")
        return created_movie
        
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))