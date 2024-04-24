from fastapi import APIRouter

from app.business.preferences.crud_preferences import create_preference, get_preference_by_id, update_preference_by_id, delete_preference_by_id

routing = APIRouter(
    prefix="/preferences",
    tags=["Preferences"]
)

routing.post("/", description="Create a new preference")(create_preference)
routing.get("/{profiles_id}", description="Get preference by id")(get_preference_by_id)
routing.put("/{profiles_id}", description="Update a preference by id")(update_preference_by_id)
routing.delete("/{profiles_id}", description="Delete a preference by id")(delete_preference_by_id)
