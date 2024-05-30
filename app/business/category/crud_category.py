from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.persistence.schemas.category_schema import CategorySchema
from app.config.connection import get_db
from app.persistence.crud.category_crud import getCategoryById, getCategories , createCategory, updateCategory, deleteCategory

def create_category(category: CategorySchema, db: Session = Depends(get_db)):
    try:
        return createCategory(db, category)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = getCategoryById(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="category not found")
    return category

def get_categories(db: Session = Depends(get_db)):
    return getCategories(db)

def update_category(category_id: int, category: CategorySchema, db: Session = Depends(get_db)):
    category = updateCategory(db, category_id, category)
    if category is None:
        raise HTTPException(status_code=404, detail="category not found")
    return category

def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = deleteCategory(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="category not found")
    return category

