from fastapi import APIRouter

from app.business.season.crud_season import get_season_by_id, update_season, get_seasons_by_series_id, create_season

routing = APIRouter(
    prefix="/seasons",
    tags=["seasons"]
)

routing.get("/{id}", description="Get season by id")(get_season_by_id)
routing.put("/{id}", description="Update season")(update_season)
routing.get("/series/{id}", description="Get seasons by series id")(get_seasons_by_series_id)
routing.post("/", description="Create season")(create_season)
