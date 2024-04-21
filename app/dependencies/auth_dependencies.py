import os
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')  # Reemplaza esto con tu clave secreta
ALGORITHM = os.getenv('ALGORITHM')  # El algoritmo que usaste para codificar el token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
# from fastapi import FastAPI, Depends
# from dependencies.auth_dependencies import verify_token

# app = FastAPI()

# @app.get("/protected-endpoint")
# async def protected_endpoint(current_user=Depends(verify_token)):
#     # Tu código aquí...
#     return {"Hello": "World"}