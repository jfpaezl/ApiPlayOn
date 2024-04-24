from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.persistence.schemas.profile_schema import ProfileSchema
from app.business.profile.crud_profile import createProfile
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

        # Crear un perfil para el usuario
        profile = ProfileSchema(
            name=user.name,
            image="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngegg.com%2Fes%2Fpng-tluen&psig=AOvVaw2Vnm4czJu49f6xu4jFWszB&ust=1713917945112000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNCgzIqI14UDFQAAAAAdAAAAABAE",
            users_id=user.id
        )
        default = createProfile(db, profile)
        if not default:
            raise HTTPException(status_code=400, detail="Error al crear el perfil")
        return {"msg": "Cuenta activada"}
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Error al activar la cuenta")
    except SQLAlchemyError:
        raise HTTPException(status_code=400, detail="Error al activar la cuenta")

# confirm_account(Depends(get_db),"g0ScxCXDjuQAeCIkt3-cUsOG-FodpdxY6JnN-iV9HfY")
