"""Módulo que define el modelo de Usuario en la base de datos."""

import enum
from sqlalchemy import Column, Integer, String, Enum
from config.db import Base

class EstadoMaterial(str, enum.Enum):
    """Enumeración para los posibles estatus del material."""
    Disponible = "Disponible"
    Prestado = "Prestado"
    Mantenimiento = "En Mantenimiento"

class Material(Base):
    """Modelo de datos para la tabla de materiales."""
    __tablename__ = "tbb_material"

    id_material = Column(Integer, primary_key=True, autoincrement=True)
    tipo_material = Column(String(100), nullable=False)
    marca = Column(String(100), nullable=True)
    modelo = Column(String(100), nullable=True)
    estado = Column(Enum(EstadoMaterial), nullable=False)