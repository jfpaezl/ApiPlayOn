from fastapi import FastAPI
from app.controllers.auth_controller import routing as authRouting

app = FastAPI()

app.include_router(authRouting)
