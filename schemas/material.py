"""Schemas para la gestión de materiales"""
from typing import Optional
from pydantic import BaseModel
from models.material import EstadoMaterial

class MaterialBase(BaseModel):
    """Esquema base para un material."""
    tipo_material: str
    marca: Optional[str]
    modelo: Optional[str]
    estado: EstadoMaterial

class MaterialCreate(MaterialBase):
    """Esquema para la creación de un material."""
    pass

class MaterialUpdate(MaterialBase):
    """Esquema para la actualización de un material."""
    pass

class Material(MaterialBase):
    """Esquema para la representación completa de un usuario."""
    id_material: int

    class Config:
        """Configuración de Pydantic para permitir la conversión desde atributos."""
        from_attributes = True
