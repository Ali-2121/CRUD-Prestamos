"""Rutas de FastAPI para la gestión de materiales."""
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import config.db
import crud.materials
import schemas.material
import models.material

material = APIRouter()

models.material.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    """Obtiene una sesión de base de datos."""
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@material.get("/materials/", response_model=List[schemas.material.Material], tags=["materiales"])
async def read_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Obtiene una lista de materiales."""
    db_materials = crud.materials.get_materials(db=db, skip=skip, limit=limit)
    return db_materials

@material.post("/material/{id}", response_model=schemas.material.Material, tags=["materiales"])
async def read_material(id: int, db: Session = Depends(get_db)):
    """Obtiene un material por su ID."""
    db_material = crud.materials.get_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

@material.post("/material/", response_model=schemas.material.Material, tags=["materiales"])
async def create_material(material: schemas.material.MaterialCreate, db: Session = Depends(get_db)):
    """Registra un nuevo material en la base de datos."""
    return crud.materials.create_material(db=db, material=material)

@material.put("/material/{id}", response_model=schemas.material.Material, tags=["materiales"])
async def update_material(
    id: int, 
    material: schemas.material.MaterialUpdate, 
    db: Session = Depends(get_db)):
    """Actualiza un material existente por su ID."""
    db_material = crud.materials.get_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return crud.materials.update_material(db=db, material=material, id=id)

@material.delete("/material/{id}", response_model=schemas.material.Material, tags=["materiales"])
async def delete_material(id: int, db: Session = Depends(get_db)):
    """Elimina un material por su ID."""
    db_material = crud.materials.get_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return crud.materials.delete_material(db=db, id=id)
