from app.models.incapacidad_model import IncapacidadModel

class IncapacidadController:
    def __init__(self):
        self.model = IncapacidadModel()

    def listar(self):
        return self.model.get_all()

    def obtener(self, id: int):
        incapacidad = self.model.get_by_id(id)
        if not incapacidad:
            return {"error": "Incapacidad no encontrada"}
        return incapacidad

    def crear(self, data: dict):
        return self.model.create(data)

    def actualizar(self, id: int, data: dict):
        return self.model.update(id, data)

    def eliminar(self, id: int):
        return self.model.delete(id)