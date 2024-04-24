from fastapi import APIRouter

from app.business.movie.crud_movie import create_movie, get_movie_by_id, update_movie, delete_movie

routing = APIRouter(
    prefix="/movie",
    tags=["movie"]
)

routing.post("/", description="Create movie")(create_movie)
routing.get("/{id}", description="Get movie by id")(get_movie_by_id)
routing.put("/{id}", description="Update movie")(update_movie)
routing.delete("/{id}", description="Delete movie")(delete_movie)

