from fastapi import APIRouter

from app.business.series.crud_series import get_series_by_id, update_series, delete_series
from app.business.series.create_serie import create_serie
from app.business.series.get_series_by_category import get_series_by_category

routing = APIRouter(
    prefix="/series",
    tags=["series"]
)

routing.post("/", description="Create series")(create_serie)
routing.get("/{id}", description="Get series by id")(get_series_by_id)
routing.get("/category/{category_id}", description="Get series by category")(get_series_by_category)
routing.put("/{id}", description="Update series")(update_series)
routing.delete("/{id}", description="Delete series")(delete_series)
