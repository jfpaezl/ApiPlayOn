from sqlalchemy.orm import Session
from app.db.movie_model import Movie
from app.persistence.schemas.movie_schema import MovieSchema, UpdateMovieSchema

def getMovieById(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()

def createMovie(db: Session, movie: MovieSchema):
    new_movie = Movie(**movie.dict())
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