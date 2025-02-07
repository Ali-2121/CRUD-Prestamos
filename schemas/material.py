from pydantic import BaseModel
from models.material import EstadoMaterial
from typing import Optional
class MaterialBase(BaseModel):
    tipo_material: str
    marca: Optional[str]
    modelo: Optional[str]
    estado: EstadoMaterial

class MaterialCreate(MaterialBase):
    pass

class MaterialUpdate(MaterialBase):
    pass

class Material(MaterialBase):
    id_material: int

    class Config:
        from_attributes = True