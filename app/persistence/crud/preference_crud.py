from sqlalchemy.orm import Session
from app.db.preference_model import Preference
from app.persistence.schemas.preference_schema import PreferenceSchema, UpdatePreferenceSchema

def createPreference(db: Session, preference: PreferenceSchema):
    db_preference = Preference(**preference.dict())
    db.add(db_preference)
    db.commit()
    db.refresh(db_preference)
    return db_preference

def getPreference(db: Session, Preferences_id: int):
    return db.query(Preference).filter(Preference.Preferences_id == Preferences_id).first()

def updatePreference(db: Session, Preferences_id: int, preference: UpdatePreferenceSchema):
    db.query(Preference).filter(Preference.Preferences_id == Preferences_id).update(preference.dict())
    db.commit()
    return db.query(Preference).filter(Preference.Preferences_id == Preferences_id).first()

def deletePreference(db: Session, Preferences_id: int):
    db.query(Preference).filter(Preference.Preferences_id == Preferences_id).delete()
    db.commit()
    return Preferences_id