"""Módulo CRUD para gestionar usuarios en la base de datos."""

import models.user
import schemas.users
from sqlalchemy.orm import Session
from datetime import datetime

def get_users(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.user.User).offset(skip).limit(limit).all()

def get_user(db: Session, id: int):
    return db.query(models.user.User).filter(models.user.User.id == id).first()

def get_user_by_usuario(db: Session, nombreUsuario: str):
    return db.query(models.user.User).filter(models.user.User.nombreUsuario == nombreUsuario).first()

def create_user(db: Session, user: schemas.users.UserCreate):
    db_user = models.user.User(
        nombre=user.nombre,
        primerApellido=user.primerApellido,
        segundoApellido=user.segundoApellido,
        tipoUsuario=user.tipoUsuario,
        nombreUsuario=user.nombreUsuario,
        correoElectronico=user.correoElectronico,
        contrasena=user.contrasena,
        nombreTelefono=user.nombreTelefono,
        status=user.status,
        fechaRegistro=datetime.utcnow(),
        fechaActualizacion=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, id: int, user: schemas.users.UserUpdate):
    db_user = db.query(models.user.User).filter(models.user.User.id == id).first()
    if db_user:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, id: int):
    db_user = db.query(models.user.User).filter(models.user.User.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
