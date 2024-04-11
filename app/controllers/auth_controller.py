from fastapi import APIRouter
from typing import List

from app.business.auth.crud_basic import create_user, get_user, get_users, update_user
from app.business.auth.login import login
from app.business.auth.confirm_account import confirm_account
from app.business.auth.change_password import forgot_password, recover_password

routing = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

routing.post("/", description="Crear usuario")(create_user)
routing.get("/", description="optener los usuarios")(get_users)
routing.get("/{id}", description="optener el usuario por id")(get_user)
routing.put("/{id}",description= "actualizar usuarios")(update_user)
routing.get("/login/", description="identificar usuario por email y contraseña verificando que estan confirmados")(login)
routing.get("/confirm/{token}", description="revisar el token para confirmar al usuario")(confirm_account)
routing.get("/forgot/{email}", description="revisar el email del usuario para recuperar contraseña")(forgot_password)
routing.post("/recover/{token}/{password}", description="revisar tonke para cambiar la contraseña")(recover_password)





