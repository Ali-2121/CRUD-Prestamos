"""Módulo CRUD para gestionar prestamos en la base de datos."""

from sqlalchemy.orm import Session
import models.prestamo
import schemas.prestamo

def get_prestamos(db: Session, skip: int = 0, limit: int = 10):
    """Función para traer todos los prestamos registrados"""
    return (db.query(models.prestamo.Prestamo)
            .offset(skip).limit(limit)
            .all())

def get_prestamo(db: Session, id: int):
    """Función para traer un prestamo buscándolo por id"""
    return (db.query(models.prestamo.Prestamo)
            .filter(models.prestamo.Prestamo.id_prestamo == id)
            .first())

def create_prestamo(db: Session, prestamo: schemas.prestamo.PrestamoCreate):
    """Función para registrar un prestamo"""
    db_prestamo = models.prestamo.Prestamo(**prestamo.dict())
    db.add(db_prestamo)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo

def update_prestamo(db: Session, prestamo: schemas.prestamo.PrestamoUpdate, id: int):
    """Función para actualizar un prestamo ya registrado"""
    db_prestamo = (db.query(models.prestamo.Prestamo)
                   .filter(models.prestamo.Prestamo.id_prestamo == id)
                   .first())
    if db_prestamo:
        for key, value in prestamo.dict(exclude_unset=True).items():
            setattr(db_prestamo, key, value)
        db.commit()
        db.refresh(db_prestamo)
    return db_prestamo

def delete_prestamo(db: Session, id: int):
    """Función para borrar un préstamo ya registrado"""
    db_prestamo = (db.query(models.prestamo.Prestamo)
                   .filter(models.prestamo.Prestamo.id_prestamo == id)
                   .first())
    if db_prestamo:
        db.delete(db_prestamo)
        db.commit()
    return db_prestamo
