from fastapi import APIRouter
from pydantic import BaseModel
from app.controllers.empleado_controller import EmpleadoController

router = APIRouter(prefix="/empleados", tags=["Empleados"])
controller = EmpleadoController()

class EmpleadoSchema(BaseModel):
    nombres: str
    apellidos: str
    documento: str
    correo: str
    telefono: str
    cargo: str
    area: str
    fecha_ingreso: str
    estado: str = "activo"

@router.get("/")
def listar_empleados():
    return controller.listar()

@router.get("/{id}")
def obtener_empleado(id: int):
    return controller.obtener(id)

@router.post("/")
def crear_empleado(data: EmpleadoSchema):
    return controller.crear(data.dict())

@router.put("/{id}")
def actualizar_empleado(id: int, data: EmpleadoSchema):
    return controller.actualizar(id, data.dict())

@router.delete("/{id}")
def eliminar_empleado(id: int):
    return controller.eliminar(id)