from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from models.user import TipoUsuario, Status

class UserBase(BaseModel):
    nombre: str
    primerApellido: str
    segundoApellido: str
    tipoUsuario: TipoUsuario
    nombreUsuario: str
    correoElectronico: str
    nombreTelefono: str
    status: Status

class UserCreate(UserBase):
    contrasena: str

class UserUpdate(UserBase):
    contrasena: Optional[str]

class User(UserBase):
    id: int
    fechaRegistro: datetime
    fechaActualizacion: datetime

    class Config:
        from_attributes = True