from sqlalchemy.orm import Session
from sqlalchemy import select, join

from app.db.moviecategory_model import MovieCategory
from app.db.category_model import Category
from ..schemas.movie_category_schema import MovieCategorySchema

def getMovieCategoryById(db: Session, movie_id: int, category_id: int):
    return db.query(MovieCategory).filter(MovieCategory.movies_id == movie_id, MovieCategory.categorys_id == category_id).first()

def createMovieCategory(db: Session, movie_category: MovieCategorySchema):
    new_movie_category = MovieCategory(**movie_category.dict())
    db.add(new_movie_category)
    db.commit()
    db.refresh(new_movie_category)
    return new_movie_category

def deleteMovieCategory(db: Session, movie_id: int, category_id: int):
    movie_category_to_delete = db.query(MovieCategory).filter(MovieCategory.movies_id == movie_id, MovieCategory.categorys_id == category_id).first()
    db.delete(movie_category_to_delete)
    db.commit()
    return movie_category_to_delete

# crear varias relaciones de categorias a una pelicula
def createMultipleMovieCategories(db: Session, movies_id: int, categorys_ids: list[int]):
    new_movie_categories = []
    for categorys_id in categorys_ids:
        new_movie_category = MovieCategory(movies_id=movies_id, categorys_id=categorys_id)
        db.add(new_movie_category)
        db.commit()
        db.refresh(new_movie_category)
        new_movie_categories.append(new_movie_category)
    return new_movie_categories

# listar las categorias por movies_id
def getCategoriesByMovieId(db: Session, movie_id: int):
    stmt = select(Category.name).select_from(
        join(MovieCategory, Category, MovieCategory.categorys_id == Category.id)
    ).where(MovieCategory.movies_id == movie_id)
    result = db.execute(stmt)
    return [row[0] for row in result.fetchall()]

# listar las peliculas por category_id
def getMoviesByCategoryId(db: Session , category_id: int):
    stmt = select(MovieCategory.movies_id).where(MovieCategory.categorys_id == category_id)
    result = db.execute(stmt)
    return [row[0] for row in result.fetchall()]

