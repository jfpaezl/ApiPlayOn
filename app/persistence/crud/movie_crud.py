from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from app.db.movie_model import Movie
from app.db.moviecategory_model import MovieCategory
from app.db.category_model import Category
from sqlalchemy import select, join
from app.persistence.schemas.movie_schema import MovieSchema, UpdateMovieSchema

def getMovieById(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()

def getMovies(db: Session):
    return db.query(Movie).order_by(func.random()).all()

def getMoviesByYear(db: Session, year: int):
    return db.query(Movie).filter(Movie.release_year == year).order_by(func.random()).all()

def createMovie(db: Session, movie: MovieSchema):
    new_movie = Movie(**movie.dict(exclude={'categories'}))
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie

def updateMovie(db: Session, movie_id: int, movie: UpdateMovieSchema):
    movie_to_update = db.query(Movie).filter(Movie.id == movie_id).first()
    for key, value in movie.dict().items():
        if value is not None:
            setattr(movie_to_update, key, value)
    db.commit()
    db.refresh(movie_to_update)
    return movie_to_update

def deleteMovie(db: Session, movie_id: int):
    movie_to_delete = db.query(Movie).filter(Movie.id == movie_id).first()
    db.delete(movie_to_delete)
    db.commit()
    return movie_to_delete

def getMoviesByDirector(db: Session, director: str):
    return db.query(Movie).filter(Movie.director == director).all()

def getMoviesByReleaseYear(db: Session, release_year: int):
    return db.query(Movie).filter(Movie.release_year == release_year).all()

def getMoviesByRecommendedAge(db: Session, recommended_age: int):
    return db.query(Movie).filter(Movie.recommended_age == recommended_age).all()

def getMoviesByCategoryId(db: Session, category_id: int):
    movies =  db.query(Movie.id, Movie.title, Movie.cover_image, Movie.is_active)\
                        .join(MovieCategory, Movie.id == MovieCategory.movies_id)\
                        .join(Category, MovieCategory.categorys_id == Category.id)\
                        .filter(Category.id == category_id).order_by(func.random()).all()
    return [movie._asdict() for movie in movies]

def getMoviesByCategoryName(db: Session, category_name: str):
    movies =  db.query(Movie.id, Movie.title, Movie.cover_image, Movie.is_active)\
                        .join(MovieCategory, Movie.id == MovieCategory.movies_id)\
                        .join(Category, MovieCategory.categorys_id == Category.id)\
                        .filter(Category.name == category_name).order_by(func.random()).all()
    return [movie._asdict() for movie in movies]



