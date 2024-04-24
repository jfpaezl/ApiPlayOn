import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.auth_controller import routing as authRouting
from app.controllers.profile_controller import routing as profileRouting
from app.controllers.movie_controller import routing as movieRouting
from app.controllers.series_controller import routing as seriesRouting
from app.controllers.preference_controller import routing as preferenceRouting

from app.config.connection import Base, engine

load_dotenv()

api_route = os.getenv("API_ROUTE")
front_route = os.getenv("FRONTEND_ROUTE")

Base.metadata.create_all(bind=engine)


app = FastAPI(title="PlayOn Api", description="API de autenticación", version="0.1.0")

# Add CORS middleware
origins = [
    api_route,
    front_route,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authRouting)
app.include_router(profileRouting)
app.include_router(movieRouting)
app.include_router(seriesRouting)
app.include_router(preferenceRouting)
