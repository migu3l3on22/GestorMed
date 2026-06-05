from app.models.seguimiento_model import SeguimientoModel

class SeguimientoController:
    def __init__(self):
        self.model = SeguimientoModel()

    def listar(self):
        return self.model.get_all()

    def obtener(self, id: int):
        seguimiento = self.model.get_by_id(id)
        if not seguimiento:
            return {"error": "Seguimiento no encontrado"}
        return seguimiento

    def crear(self, data: dict):
        return self.model.create(data)

    def actualizar(self, id: int, data: dict):
        return self.model.update(id, data)

    def eliminar(self, id: int):
        return self.model.delete(id)