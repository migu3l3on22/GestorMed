from database import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def get_all(self):
        self.db.connect()
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, correo, usuario, rol, estado FROM usuarios")
        result = cursor.fetchall()
        self.db.disconnect()
        return result

    def get_by_id(self, id: int):
        self.db.connect()
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, correo, usuario, rol, estado FROM usuarios WHERE id = %s", (id,))
        result = cursor.fetchone()
        self.db.disconnect()
        return result

    def create(self, data: dict):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, correo, usuario, contrasena, rol) VALUES (%s, %s, %s, %s, %s)",
            (data["nombre"], data["correo"], data["usuario"], data["contrasena"], data["rol"])
        )
        self.db.connection.commit()
        self.db.disconnect()
        return {"mensaje": "Usuario creado correctamente"}

    def update(self, id: int, data: dict):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            "UPDATE usuarios SET nombre=%s, correo=%s, rol=%s, estado=%s WHERE id=%s",
            (data["nombre"], data["correo"], data["rol"], data["estado"], id)
        )
        self.db.connection.commit()
        self.db.disconnect()
        return {"mensaje": "Usuario actualizado"}

    def delete(self, id: int):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
        self.db.connection.commit()
        self.db.disconnect()
        return {"mensaje": "Usuario eliminado"}