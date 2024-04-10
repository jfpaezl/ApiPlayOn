from fastapi import Depends, HTTPException
import secrets
from typing import Union
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from app.utils.hash import hash_password
from app.persistence.crud.user_crud import createUser, getUser, getUsers, updateUser
from app.config.connection import get_db, engine, Base
from app.persistence.schemas.user_schema import UserUpdateSchema, UserCreateSchema

Base.metadata.create_all(bind=engine)


def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    try: 
        newUser = user
        newUser.password = hash_password(user.password)
        newUser.token = secrets.token_urlsafe(32)
        return createUser(db, user)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Email already in use")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_user(id: int, db: Session = Depends(get_db)):
    try:
        user = getUser(db, id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        return getUsers(db, skip, limit)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_user(id: int, user:Union[UserUpdateSchema, dict], db: Session = Depends(get_db)):
    try:
        userToUpdate = updateUser(db, id, user)
        if userToUpdate is None:
            raise HTTPException(status_code=404, detail="User not found")
        return userToUpdate
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

# print(create_user(
#    { 
#         'name': 'jfpaezl2',
#         'email': 'jfpaezl2@email.com',
#         'password': '123456'
#     } 
# ))

