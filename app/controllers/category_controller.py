from fastapi import APIRouter

from app.business.category.crud_category import create_category, get_category_by_id, update_category, delete_category

routing = APIRouter(
    prefix="/category",
    tags=["category"]
)

routing.post("/", description="Create a category")(create_category)
routing.get("/{id}", description="Get a category by id")(get_category_by_id)
routing.put("/{id}", description="Update a category")(update_category)
routing.delete("/{id}", description="Delete a category")(delete_category)