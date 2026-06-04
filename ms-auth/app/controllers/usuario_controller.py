from app.models.usuario_model import UsuarioModel

class UsuarioController:
    def __init__(self):
        self.model = UsuarioModel()

    def listar(self):
        return self.model.get_all()

    def obtener(self, id: int):
        usuario = self.model.get_by_id(id)
        if not usuario:
            return {"error": "Usuario no encontrado"}
        return usuario

    def crear(self, data: dict):
        return self.model.create(data)

    def actualizar(self, id: int, data: dict):
        return self.model.update(id, data)

    def eliminar(self, id: int):
        return self.model.delete(id)