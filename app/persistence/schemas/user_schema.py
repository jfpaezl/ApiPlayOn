from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
    name: str
    email: EmailStr

class UserCreateSchema(UserSchema):
    password: str = Field(..., min_length=6, max_length=100),
    token: Optional[str] = None

class UserUpdateSchema(UserSchema):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None 
    confirm: Optional[bool] = None
    token: Optional[str] = None
    updatedAt: Optional[datetime] = None

class UserDedailSchema(UserSchema):
    id: int
    createdAt: datetime
    updatedAt: datetime
    confirm: Optional[bool] = False
    token: Optional[str] = None

class ChangePasswordSchema(BaseModel):
    password: str = Field(..., min_length=6, max_length=100)
    new_password: str = Field(..., min_length=6, max_length=100)
    email: EmailStr 



