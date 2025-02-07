"""Schemas para la gestión de usuarios"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from models.user import TipoUsuario, Status

class UserBase(BaseModel):
    """Esquema base para un usuario."""
    nombre: str
    primerApellido: str
    segundoApellido: str
    tipoUsuario: TipoUsuario
    nombreUsuario: str
    correoElectronico: str
    nombreTelefono: str
    status: Status

class UserCreate(UserBase):
    """Esquema para la creación de un usuario."""
    contrasena: str

class UserUpdate(UserBase):
    """Esquema para la actualización de un usuario."""
    contrasena: Optional[str]

class User(UserBase):
    """Esquema para la representación completa de un usuario."""
    id: int
    fechaRegistro: datetime
    fechaActualizacion: datetime

    class Config:
        """Configuración de Pydantic para permitir la conversión desde atributos."""
        from_attributes = True
