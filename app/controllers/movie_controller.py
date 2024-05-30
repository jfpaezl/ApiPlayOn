from fastapi import APIRouter

from app.business.movie.crud_movie import get_movie_by_id, update_movie, delete_movie, get_movies_by_release_year, get_Movies
from app.business.movie.create_movie import create_movie
from app.business.movie.get_movies_by_category import get_movies_by_category, get_movies_by_category_name

routing = APIRouter(
    prefix="/movie",
    tags=["movie"]
)

routing.post("/", description="Create movie")(create_movie)
routing.get("/{id}", description="Get movie by id")(get_movie_by_id)
routing.get("/", description="Get movies")(get_Movies)
routing.get("/year/{year}", description="Get movies by year")(get_movies_by_release_year)
routing.get("/category/name/{category_name}", description="Get movies by category name")(get_movies_by_category_name)
routing.get("/category/{category_id}", description="Get movies by category")(get_movies_by_category)
routing.put("/{id}", description="Update movie")(update_movie)
routing.delete("/{id}", description="Delete movie")(delete_movie)


