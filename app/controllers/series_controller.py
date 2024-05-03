from fastapi import APIRouter

from app.business.series.crud_series import get_series_by_id, update_series, delete_series
from app.business.series.create_serie import create_serie

routing = APIRouter(
    prefix="/series",
    tags=["series"]
)

routing.post("/", description="Create series")(create_serie)
routing.get("/{id}", description="Get series by id")(get_series_by_id)
routing.put("/{id}", description="Update series")(update_series)
routing.delete("/{id}", description="Delete series")(delete_series)
