"""Rutas de FastAPI para la gestión de prestamos."""
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import config.db
import crud.prestamos
import schemas.prestamo
import models.prestamo

prestamo = APIRouter()

models.prestamo.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    """Obtiene una sesión de base de datos."""
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@prestamo.get("/prestamos/", response_model=List[schemas.prestamo.Prestamo], tags=["prestamos"])
async def read_prestamos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    ''' Se obtienen los datos de los prestamos '''
    db_prestamos = crud.prestamos.get_prestamos(db=db, skip=skip, limit=limit)
    return db_prestamos

@prestamo.post("/prestamo/{id}", response_model=schemas.prestamo.Prestamo, tags=["prestamos"])
async def read_prestamo(id: int, db: Session = Depends(get_db)):
    ''' Post que trae los prestamos por id'''
    db_prestamo = crud.prestamos.get_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return db_prestamo

@prestamo.post("/prestamo/", response_model=schemas.prestamo.Prestamo, tags=["prestamos"])
async def create_prestamo(prestamo: schemas.prestamo.PrestamoCreate, db: Session = Depends(get_db)):
    ''' Registrar prestamo '''
    return crud.prestamos.create_prestamo(db=db, prestamo=prestamo)

@prestamo.put("/prestamo/{id}", response_model=schemas.prestamo.Prestamo, tags=["prestamos"])
async def update_prestamo(
    id: int,
    prestamo: schemas.prestamo.PrestamoUpdate,
    db: Session = Depends(get_db)):
    ''' Actualizar prestamo '''
    db_prestamo = crud.prestamos.get_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return crud.prestamos.update_prestamo(db=db, prestamo=prestamo, id=id)

@prestamo.delete("/prestamo/{id}", response_model=schemas.prestamo.Prestamo, tags=["prestamos"])
async def delete_prestamo(id: int, db: Session = Depends(get_db)):
    ''' Eliminar prestamo '''
    db_prestamo = crud.prestamos.get_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return crud.prestamos.delete_prestamo(db=db, id=id)
