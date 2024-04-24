from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.persistence.schemas.preference_schema import PreferenceSchema, UpdatePreferenceSchema
from app.config.connection import get_db
from app.persistence.crud.preference_crud import createPreference, getPreference, updatePreference, deletePreference

def create_preference(preference: PreferenceSchema, db: Session = Depends(get_db)):
    try:
        return createPreference(db, preference)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
def get_preference_by_id(preference_id: int, db: Session = Depends(get_db)):
    preference = getPreference(db, preference_id)
    if preference is None:
        raise HTTPException(status_code=404, detail="Preference not found")
    return preference

def update_preference_by_id(preference_id: int, preference: UpdatePreferenceSchema, db: Session = Depends(get_db)):
    preference = updatePreference(db, preference_id, preference)
    if preference is None:
        raise HTTPException(status_code=404, detail="Preference not found")
    return preference

def delete_preference_by_id(preference_id: int, db: Session = Depends(get_db)):
    preference = deletePreference(db, preference_id)
    if preference is None:
        raise HTTPException(status_code=404, detail="Preference not found")
    return preference

