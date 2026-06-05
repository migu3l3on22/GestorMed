from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from app.controllers.incapacidad_controller import IncapacidadController

router = APIRouter(prefix="/incapacidades", tags=["Incapacidades"])
controller = IncapacidadController()

class IncapacidadSchema(BaseModel):
    empleado_id: int
    fecha_inicio: str
    fecha_fin: str
    tipo: str
    diagnostico_general: str
    entidad_medica: str
    observaciones: Optional[str] = None
    dias_incapacidad: int
    estado: str = "registrada"

@router.get("/")
def listar_incapacidades():
    return controller.listar()

@router.get("/{id}")
def obtener_incapacidad(id: int):
    return controller.obtener(id)

@router.post("/")
def crear_incapacidad(data: IncapacidadSchema):
    return controller.crear(data.dict())

@router.put("/{id}")
def actualizar_incapacidad(id: int, data: IncapacidadSchema):
    return controller.actualizar(id, data.dict())

@router.delete("/{id}")
def eliminar_incapacidad(id: int):
    return controller.eliminar(id)