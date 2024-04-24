from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.persistence.schemas.profile_schema import ProfileSchema, UpdateProfileSchema
from app.config.connection import get_db
from app.persistence.crud.profile_crud import createProfile, getProfileById, getProfilesByUserId, updateProfile, deleteProfile

def create_profile(profile: ProfileSchema, db : Session = Depends(get_db)):
    try:
        return createProfile(db, profile)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def get_profile_by_id(profile_id: int, db : Session = Depends(get_db)):
    try:
        profile = getProfileById(db, profile_id)
        if profile is None:
            raise HTTPException(status_code=404, detail="Profile not found")
        return profile
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_profiles_by_user_id(user_id: int, db : Session = Depends(get_db)):
    try:
        profiles = getProfilesByUserId(db, user_id)
        if profiles is None:
            raise HTTPException(status_code=404, detail="Profiles not found")
        return profiles
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_profile(profile_id: int, profile: UpdateProfileSchema, db : Session = Depends(get_db)):
    try:
        profile_to_update = getProfileById(db, profile_id)
        if profile_to_update is None:
            raise HTTPException(status_code=404, detail="Profile not found")
        return updateProfile(db, profile_id, profile)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_profile(profile_id: int, db : Session = Depends(get_db)):
    try:
        profile = getProfileById(db, profile_id)
        if profile is None:
            raise HTTPException(status_code=404, detail="Profile not found")
        return deleteProfile(db, profile_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    