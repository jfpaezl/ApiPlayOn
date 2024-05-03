from fastapi import APIRouter

from app.business.episodes.crud_episodes import create_episode, get_episode_by_id, get_episodes_by_season_id, update_episode

routing = APIRouter(
    prefix="/episodes",
    tags=["episodes"]
)

routing.post("/", description="Create an episode")(create_episode)
routing.get("/{id}", description="Get an episode by id")(get_episode_by_id)
routing.get("/season/{id}", description="Get episodes by season id")(get_episodes_by_season_id)
routing.put("/{id}", description="Update an episode")(update_episode)

