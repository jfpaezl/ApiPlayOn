import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.auth_controller import routing as authRouting
from app.config.connection import Base, engine

load_dotenv()

api_route = os.getenv("API_ROUTE")
front_route = os.getenv("FRONTEND_ROUTE")

Base.metadata.create_all(bind=engine)


app = FastAPI()

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
