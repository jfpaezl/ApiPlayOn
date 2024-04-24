from fastapi import APIRouter

from app.business.profile.crud_profile import create_profile, get_profile_by_id, get_profiles_by_user_id, update_profile, delete_profile

routing = APIRouter(
    prefix="/profile",
    tags=["profile"]
)

routing.post("/", description="Create profile")(create_profile)
routing.get("/{id}", description="Get profile by id")(get_profile_by_id)
routing.get("/user/{user_id}", description="Get profiles by user id")(get_profiles_by_user_id)
routing.put("/{id}", description="Update profile")(update_profile)
routing.delete("/{id}", description="Delete profile")(delete_profile)