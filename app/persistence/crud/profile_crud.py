from sqlalchemy.orm import Session
from app.db.profile_model import Profile
from app.persistence.schemas.profile_schema import ProfileSchema, UpdateProfileSchema

def getProfileById(db: Session, profile_id: int):
    return db.query(Profile).filter(Profile.id == profile_id).first()

def createProfile(db: Session, profile: ProfileSchema):
    new_profile = Profile(**profile.dict())
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

def updateProfile(db: Session, profile_id: int, profile: UpdateProfileSchema):
    profile_to_update = db.query(Profile).filter(Profile.id == profile_id).first()
    for key, value in profile.dict().items():
        if value is not None:
            setattr(profile_to_update, key, value)
    db.commit()
    db.refresh(profile_to_update)
    return profile_to_update

def deleteProfile(db: Session, profile_id: int):
    profile_to_delete = db.query(Profile).filter(Profile.id == profile_id).first()
    db.delete(profile_to_delete)
    db.commit()
    return profile_to_delete

def getProfilesByUserId(db: Session, user_id: int):
    return db.query(Profile).filter(Profile.users_id == user_id).all()