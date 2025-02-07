from pydantic import BaseModel
from datetime import datetime
from models.prestamo import EstadoPrestamo
from typing import Optional

class PrestamoBase(BaseModel):
    id_usuario: int
    id_material: int
    fecha_prestamo: datetime
    fecha_devolucion: Optional[datetime]
    estado: EstadoPrestamo

class PrestamoCreate(PrestamoBase):
    pass

class PrestamoUpdate(PrestamoBase):
    pass

class Prestamo(PrestamoBase):
    id_prestamo: int

    class Config:
        from_attributes = True