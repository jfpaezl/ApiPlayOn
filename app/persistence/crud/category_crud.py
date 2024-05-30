from sqlalchemy.orm import Session
from app.db.category_model import Category
from ..schemas.category_schema import CategorySchema

def getCategoryById (db:Session, category_id:int):
    return db.query(Category).filter(Category.id == category_id).first()

def getCategories (db:Session):
    return db.query(Category).all()

def createCategory (db:Session, category:CategorySchema):
    new_category = Category(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def updateCategory (db:Session, category_id:int, category:CategorySchema):
    category_to_update = db.query(Category).filter(Category.id == category_id).first()
    for key, value in category.dict().items():
        if value is not None:
            setattr(category_to_update, key, value)
    db.commit()
    db.refresh(category_to_update)
    return category_to_update

def deleteCategory (db:Session, category_id:int):
    category_to_delete = db.query(Category).filter(Category.id == category_id).first()
    db.delete(category_to_delete)
    db.commit()
    return category_to_delete
