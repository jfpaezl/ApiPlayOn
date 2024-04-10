from sqlalchemy.orm import Session
from datetime import datetime
from app.db.user_model import User
from app.persistence.schemas.user_schema import UserUpdateSchema, UserCreateSchema



def createUser(db: Session, user: UserCreateSchema):
    newUser = User(**user.dict())
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

def getUser(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def getUsers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def updateUser(db: Session, id: int, user: UserUpdateSchema):
    userToUpdate = db.query(User).filter(User.id == id).first()
    userToUpdate.updatedAt = datetime.now()
    for key, value in user.dict().items():
        if value is not None:
            setattr(userToUpdate, key, value)
    db.commit()
    db.refresh(userToUpdate)
    return userToUpdate

def getByToken(db: Session, token: str):
    return db.query(User).filter(User.token == token).first()

def authenticate_user(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user