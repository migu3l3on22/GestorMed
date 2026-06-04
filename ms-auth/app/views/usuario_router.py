from fastapi import APIRouter
from pydantic import BaseModel
from app.controllers.usuario_controller import UsuarioController

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])
controller = UsuarioController()

class UsuarioSchema(BaseModel):
    nombre: str
    correo: str
    usuario: str
    contrasena: str
    rol: str
    estado: str = "activo"

@router.get("/")
def listar_usuarios():
    return controller.listar()

@router.get("/{id}")
def obtener_usuario(id: int):
    return controller.obtener(id)

@router.post("/")
def crear_usuario(data: UsuarioSchema):
    return controller.crear(data.dict())

@router.put("/{id}")
def actualizar_usuario(id: int, data: UsuarioSchema):
    return controller.actualizar(id, data.dict())

@router.delete("/{id}")
def eliminar_usuario(id: int):
    return controller.eliminar(id)