from app.models.empleado_model import EmpleadoModel

class EmpleadoController:
    def __init__(self):
        self.model = EmpleadoModel()

    def listar(self):
        return self.model.get_all()

    def obtener(self, id: int):
        empleado = self.model.get_by_id(id)
        if not empleado:
            return {"error": "Empleado no encontrado"}
        return empleado

    def crear(self, data: dict):
        return self.model.create(data)

    def actualizar(self, id: int, data: dict):
        return self.model.update(id, data)

    def eliminar(self, id: int):
        return self.model.delete(id)