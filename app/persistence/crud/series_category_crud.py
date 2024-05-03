from sqlalchemy.orm import Session
from sqlalchemy import select, join

from app.db.seriescategory_model import SeriesCategory
from app.db.category_model import Category
from ..schemas.series_category_schema import SeriesCategorySchema

def getSeriesCategoryById(db: Session, series_id: int, category_id: int):
    return db.query(SeriesCategory).filter(SeriesCategory.series_id == series_id, SeriesCategory.category_id == category_id).first()

def createSeriesCategory(db: Session, series_category: SeriesCategorySchema):
    new_series_category = SeriesCategory(**series_category.dict())
    db.add(new_series_category)
    db.commit()
    db.refresh(new_series_category)
    return new_series_category

def deleteSeriesCategory(db: Session, series_id: int, category_id: int):
    series_category_to_delete = db.query(SeriesCategory).filter(SeriesCategory.series_id == series_id, SeriesCategory.category_id == category_id).first()
    db.delete(series_category_to_delete)
    db.commit()
    return series_category_to_delete

# crear varias relaciones de categorias a una serie
def createMultipleSeriesCategories(db: Session, series_categories: list[SeriesCategorySchema]):
    new_series_categories = []
    for series_category in series_categories:
        new_series_category = SeriesCategory(**series_category.dict())
        db.add(new_series_category)
        db.commit()
        db.refresh(new_series_category)
        new_series_categories.append(new_series_category)
    return new_series_categories

# listar las categorias por series_id
def getCategoriesBySeriesId(db: Session, series_id: int):
    stmt = select(Category.name).select_from(
        join(SeriesCategory, Category, SeriesCategory.categorys_id == Category.id)
    ).where(SeriesCategory.series_id == series_id)
    result = db.execute(stmt)
    return [row[0] for row in result.fetchall()]