from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.persistence.schemas.movie_schema import MovieSchema, UpdateMovieSchema
from app.config.connection import get_db
from app.persistence.crud.movie_crud import getMovieById, updateMovie, deleteMovie, getMoviesByReleaseYear, getMovies
from app.persistence.crud.movie_category_crud import getCategoriesByMovieId

    
def get_movie_by_id(movie_id: int, db : Session = Depends(get_db)):
    try:
        movie = getMovieById(db, movie_id)
        if movie:
            movie.categories = getCategoriesByMovieId(db, movie_id)
        if movie is None:
            raise HTTPException(status_code=404, detail="Movie not found")
        return movie
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_Movies(db : Session = Depends(get_db)):
    try:
        movies = getMovies(db)
        return movies
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_movies_by_release_year(release_year: int, db : Session = Depends(get_db)):
    try:
        movies = getMoviesByReleaseYear(db, release_year)
        if not movies:
            raise HTTPException(status_code=404, detail="No movies found for the given year")
        return movies
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


def update_movie(movie_id: int, movie: UpdateMovieSchema, db : Session = Depends(get_db)):
    try:
        movie_to_update = getMovieById(db, movie_id)
        if movie_to_update is None:
            raise HTTPException(status_code=404, detail="Movie not found")
        return updateMovie(db, movie_id, movie)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_movie(movie_id: int, db : Session = Depends(get_db)):
    try:
        movie = getMovieById(db, movie_id)
        if movie is None:
            raise HTTPException(status_code=404, detail="Movie not found")
        return deleteMovie(db, movie_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    

