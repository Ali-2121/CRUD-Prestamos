"""Schemas para la gestión de prestamos"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from models.prestamo import EstadoPrestamo

class PrestamoBase(BaseModel):
    """Esquema base para un prestamo."""
    id_usuario: int
    id_material: int
    fecha_prestamo: datetime
    fecha_devolucion: Optional[datetime]
    estado: EstadoPrestamo

class PrestamoCreate(PrestamoBase):
    """Esquema para la creación de un prestamo."""
    pass

class PrestamoUpdate(PrestamoBase):
    """Esquema para la actualización de un prestamo."""
    pass

class Prestamo(PrestamoBase):
    """Esquema para la representación completa de un prestamo."""
    id_prestamo: int

    class Config:
        """Configuración de Pydantic para permitir la conversión desde atributos."""
        from_attributes = True
