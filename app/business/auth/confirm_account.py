from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from app.config.connection import get_db
from app.persistence.crud.user_crud import getByToken

def confirm_account(token: str, db: Session = Depends(get_db)):
    # veificar que algun usuario si tenga el token
    user = getByToken(db, token)
    
    if not user:
        raise HTTPException(status_code=404, detail="Token no encontrado")
    try:
        user.confirm=True
        user.token=None
        db.commit()
        db.refresh(user)
        return {"msg": "Cuenta activada"}
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Error al activar la cuenta")
    except SQLAlchemyError:
        raise HTTPException(status_code=400, detail="Error al activar la cuenta")

# confirm_account(Depends(get_db),"g0ScxCXDjuQAeCIkt3-cUsOG-FodpdxY6JnN-iV9HfY")
