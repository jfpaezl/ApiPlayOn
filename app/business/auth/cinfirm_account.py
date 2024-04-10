from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from app.persistence.schemas.user_schema import UserDedailSchema
from app.config.connection import get_db
from app.persistence.crud.user_crud import getByToken

def confirm_account(token: str, db: Session = Depends(get_db)):
    # veificar que algun usuario si tenga el token
    user = getByToken(db, token)
    
    if not user:
        raise HTTPException(status_code=404, detail="Token no encontrado")
    try:
        # activar la cuenta
        user.confirm = True

        # Eliminar el token
        user.token = None

        # Guardar los cambios
        db.commit()
        db.refresh(user)
        return UserDedailSchema(**user.__dict__)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Error al activar la cuenta")
    except SQLAlchemyError:
        raise HTTPException(status_code=400, detail="Error al activar la cuenta")

# confirm_account(Depends(get_db),"g0ScxCXDjuQAeCIkt3-cUsOG-FodpdxY6JnN-iV9HfY")
