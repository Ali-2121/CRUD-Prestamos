"""Módulo CRUD para gestionar materiales en la base de datos."""

from sqlalchemy.orm import Session
import models.material
import schemas.material

def get_materials(db: Session, skip: int = 0, limit: int = 10):
    """Obtiene Todos los materiales."""
    return (db.query(models.material.Material).
            offset(skip)
            .limit(limit)
            .all())

def get_material(db: Session, id: int):
    """Obtiene solo un material buscando por su id."""
    return (db.query(models.material.Material)
            .filter(models.material.Material.id_material == id)
            .first())

def create_material(db: Session, material: schemas.material.MaterialCreate):
    """Crea el registro de un material."""
    db_material = models.material.Material(**material.dict())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def update_material(db: Session, material: schemas.material.MaterialUpdate, id: int):
    """Actualiza la información de un material, buscandolo primero por su id."""
    db_material = (db.query(models.material.Material)
                   .filter(models.material.Material.id_material == id)
                   .first()
    )
    if db_material:
        for key, value in material.dict(exclude_unset=True).items():
            setattr(db_material, key, value)
        db.commit()
        db.refresh(db_material)
    return db_material

def delete_material(db: Session, id: int):
    """Borra un material, buscándolo por su id."""
    db_material = (db.query(models.material.Material)
                   .filter(models.material.Material.id_material == id)
                   .first()
    )
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
