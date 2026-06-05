from database import Database

class SeguimientoModel:
    def __init__(self):
        self.db = Database()

    def get_all(self):
        self.db.connect()
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM seguimientos")
        result = cursor.fetchall()
        self.db.disconnect()
        return result

    def get_by_id(self, id: int):
        self.db.connect()
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM seguimientos WHERE id = %s", (id,))
        result = cursor.fetchone()
        self.db.disconnect()
        return result

    def create(self, data: dict):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            """INSERT INTO seguimientos 
            (incapacidad_id, fecha, comentario, estado, usuario_responsable) 
            VALUES (%s, %s, %s, %s, %s)""",
            (data["incapacidad_id"], data["fecha"], data["comentario"],
             data["estado"], data["usuario_responsable"])
        )
        self.db.connection.commit()
        self.db.disconnect()
        return {"mensaje": "Seguimiento creado correctamente"}

    def update(self, id: int, data: dict):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            """UPDATE seguimientos SET fecha=%s, comentario=%s,
            estado=%s, usuario_responsable=%s WHERE id=%s""",
            (data["fecha"], data["comentario"],
             data["estado"], data["usuario_responsable"], id)
        )
        self.db.connection.commit()
        self.db.disconnect()
        return {"mensaje": "Seguimiento actualizado"}

    def delete(self, id: int):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute("DELETE FROM seguimientos WHERE id = %s", (id,))
        self.db.connection.commit()
        self.db.disconnect()
        return {"mensaje": "Seguimiento eliminado"}