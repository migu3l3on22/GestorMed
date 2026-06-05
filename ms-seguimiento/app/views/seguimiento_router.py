from fastapi import APIRouter
from pydantic import BaseModel
from app.controllers.seguimiento_controller import SeguimientoController

router = APIRouter(prefix="/seguimientos", tags=["Seguimientos"])
controller = SeguimientoController()

class SeguimientoSchema(BaseModel):
    incapacidad_id: int
    fecha: str
    comentario: str
    estado: str
    usuario_responsable: str

@router.get("/")
def listar_seguimientos():
    return controller.listar()

@router.get("/{id}")
def obtener_seguimiento(id: int):
    return controller.obtener(id)

@router.post("/")
def crear_seguimiento(data: SeguimientoSchema):
    return controller.crear(data.dict())

@router.put("/{id}")
def actualizar_seguimiento(id: int, data: SeguimientoSchema):
    return controller.actualizar(id, data.dict())

@router.delete("/{id}")
def eliminar_seguimiento(id: int):
    return controller.eliminar(id)