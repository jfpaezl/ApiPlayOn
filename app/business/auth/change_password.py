import os
import secrets
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from dotenv import load_dotenv

from app.persistence.schemas.user_schema import ChangePasswordSchema
from app.persistence.crud.user_crud import authenticate_user, getByToken
from app.config.connection import get_db
from app.utils.hash import verify_password
from app.utils.confirm_email import send_confirmation_email

load_dotenv()

router = os.getenv("API_ROUTE")
def change_password(data: ChangePasswordSchema, db: Session = Depends(get_db)):
    try:
        user = authenticate_user(data.email, db)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        if not verify_password(data.password, user.password):
            raise HTTPException(status_code=401, detail="Incorrect password")
        user.password = data.new_password
        db.commit()
        db.refresh(user)
        return user
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def recover_password (token: str, password: str, db: Session = Depends(get_db)):
    try:
        user = getByToken(db, token)
        if user is None:
            raise HTTPException(status_code=404, detail="Token not found")
        user.password = password
        user.token = None
        db.commit()
        db.refresh(user)
        return user
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def forgot_password(email: str, db: Session = Depends(get_db)):
    try:
        user = authenticate_user(email, db)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        if not user.confirm:
            raise HTTPException(status_code=401, detail="User not confirmed")
        user.token = secrets.token_urlsafe(32)
        db.commit()
        send_confirmation_email(user.email, f"{router}/auth/reset/{user.token}")
        return {"msg": "Email sent"}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))