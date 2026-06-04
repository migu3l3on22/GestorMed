from database import Database

class EmpleadoModel:
    def __init__(self):
        self.db = Database()

    def get_all(self):
        self.db.connect()
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM empleados")
        result = cursor.fetchall()
        self.db.disconnect()
        return result

    def get_by_id(self, id: int):
        self.db.connect()
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM empleados WHERE id = %s", (id,))
        result = cursor.fetchone()
        self.db.disconnect()
        return result

    def create(self, data: dict):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            """INSERT INTO empleados 
            (nombres, apellidos, documento, correo, telefono, cargo, area, fecha_ingreso) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (data["nombres"], data["apellidos"], data["documento"],
             data["correo"], data["telefono"], data["cargo"],
             data["area"], data["fecha_ingreso"])
        )
        self.db.connection.commit()
        self.db.disconnect()
        return {"mensaje": "Empleado creado correctamente"}

    def update(self, id: int, data: dict):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            """UPDATE empleados SET nombres=%s, apellidos=%s, correo=%s,
            telefono=%s, cargo=%s, area=%s, estado=%s WHERE id=%s""",
            (data["nombres"], data["apellidos"], data["correo"],
             data["telefono"], data["cargo"], data["area"],
             data["estado"], id)
        )
        self.db.connection.commit()
        self.db.disconnect()
        return {"mensaje": "Empleado actualizado"}

    def delete(self, id: int):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute("DELETE FROM empleados WHERE id = %s", (id,))
        self.db.connection.commit()
        self.db.disconnect()
        return {"mensaje": "Empleado eliminado"}