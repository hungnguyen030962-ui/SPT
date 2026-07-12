from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.literature import LiteratureMaterial
from app.schemas.literature import LiteratureMaterialCreate
from typing import Optional

def get_literature_material(db: Session, material_id: int):
    return db.query(LiteratureMaterial).filter(LiteratureMaterial.id == material_id).first()

def get_literature_materials(
    db: Session,
    search: Optional[str] = None,
    skip: int = 0,
    limit: int = 100
):
    query = db.query(LiteratureMaterial)
    if search:
        query = query.filter(
            or_(
                LiteratureMaterial.title.ilike(f"%{search}%"),
                LiteratureMaterial.author.ilike(f"%{search}%"),
                LiteratureMaterial.epoch.ilike(f"%{search}%")
            )
        )
    return query.offset(skip).limit(limit).all()

def create_literature_material(db: Session, material: LiteratureMaterialCreate):
    db_material = LiteratureMaterial(**material.model_dump())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material
