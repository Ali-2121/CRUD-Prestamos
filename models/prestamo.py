"""Módulo que define el modelo de préstamos en la base de datos."""

import enum
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from config.db import Base

class EstadoPrestamo(str, enum.Enum):
    """Enumeración para los estados de un préstamo."""
    Activo = "Activo"
    Devuelto = "Devuelto"
    Vencido = "Vencido"

class Prestamo(Base):
    """Modelo de datos para la tabla de préstamos."""
    __tablename__ = "tbb_prestamo"

    id_prestamo = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('tbb_usuario.id'), nullable=False)
    id_material = Column(Integer, ForeignKey('tbb_material.id_material'), nullable=False)
    fecha_prestamo = Column(DateTime, nullable=False)
    fecha_devolucion = Column(DateTime, nullable=True)
    estado = Column(Enum(EstadoPrestamo), nullable=False)
