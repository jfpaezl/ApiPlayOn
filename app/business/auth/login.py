from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.persistence.crud.user_crud import authenticate_user
from app.config.connection import get_db
from app.utils.hash import verify_password
from app.utils.jwt import create_access_token


def login (email: str, password: str, db : Session = Depends(get_db)):
    try:
        user = authenticate_user(email, db)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        if not verify_password(str(password), user.password):
            raise HTTPException(status_code=401, detail="Incorrect password")
        if not user.confirm:
            raise HTTPException(status_code=401, detail="User not confirmed")
        
        token_data = {"user":user.id,"email": user.email,"name": user.name}
        token = create_access_token(data=token_data)
        return {'token' : token, 'user': {'id': user.id, 'email': user.email, 'name': user.name}}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

