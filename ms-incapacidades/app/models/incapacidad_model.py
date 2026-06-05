from database import Database

class IncapacidadModel:
    def __init__(self):
        self.db = Database()

    def get_all(self):
        self.db.connect()
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM incapacidades")
        result = cursor.fetchall()
        self.db.disconnect()
        return result

    def get_by_id(self, id: int):
        self.db.connect()
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM incapacidades WHERE id = %s", (id,))
        result = cursor.fetchone()
        self.db.disconnect()
        return result

    def create(self, data: dict):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            """INSERT INTO incapacidades 
            (empleado_id, fecha_inicio, fecha_fin, tipo, diagnostico_general, entidad_medica, observaciones, dias_incapacidad) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (data["empleado_id"], data["fecha_inicio"], data["fecha_fin"],
             data["tipo"], data["diagnostico_general"], data["entidad_medica"],
             data["observaciones"], data["dias_incapacidad"])
        )
        self.db.connection.commit()
        self.db.disconnect()
        return {"mensaje": "Incapacidad creada correctamente"}

    def update(self, id: int, data: dict):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            """UPDATE incapacidades SET fecha_inicio=%s, fecha_fin=%s, tipo=%s,
            diagnostico_general=%s, entidad_medica=%s, observaciones=%s,
            dias_incapacidad=%s, estado=%s WHERE id=%s""",
            (data["fecha_inicio"], data["fecha_fin"], data["tipo"],
             data["diagnostico_general"], data["entidad_medica"],
             data["observaciones"], data["dias_incapacidad"],
             data["estado"], id)
        )
        self.db.connection.commit()
        self.db.disconnect()
        return {"mensaje": "Incapacidad actualizada"}

    def delete(self, id: int):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute("DELETE FROM incapacidades WHERE id = %s", (id,))
        self.db.connection.commit()
        self.db.disconnect()
        return {"mensaje": "Incapacidad eliminada"}