from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud import literature as crud_literature
from app.schemas.literature import LiteratureMaterialOut
from typing import List, Optional

router = APIRouter(prefix="/literature", tags=["literature"])

@router.get("/materials", response_model=List[LiteratureMaterialOut])
def read_materials(
    search: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud_literature.get_literature_materials(db, search=search, skip=skip, limit=limit)

@router.get("/materials/{material_id}", response_model=LiteratureMaterialOut)
def read_material(material_id: int, db: Session = Depends(get_db)):
    material = crud_literature.get_literature_material(db, material_id=material_id)
    if not material:
        raise HTTPException(status_code=404, detail="Literature material not found")
    return material
