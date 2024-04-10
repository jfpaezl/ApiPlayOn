from fastapi import APIRouter
from typing import List

from app.business.auth.crud_basic import create_user, get_user, get_users, update_user
from app.business.auth.login import login
from app.business.auth.cinfirm_account import confirm_account

routing = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

routing.post("/")(create_user)
routing.get("/")(get_users)
routing.get("/{id}")(get_user)
routing.put("/{id}")(update_user)
routing.get("/login/")(login)
routing.get("/confirm/{token}")(confirm_account)




