from fastapi import APIRouter

from app.business.series.crud_series import create_series, get_series_by_id, update_series, delete_series

routing = APIRouter(
    prefix="/series",
    tags=["series"]
)

routing.post("/", description="Create series")(create_series)
routing.get("/{id}", description="Get series by id")(get_series_by_id)
routing.put("/{id}", description="Update series")(update_series)
routing.delete("/{id}", description="Delete series")(delete_series)
