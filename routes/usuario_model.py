import psycopg2
from psycopg2.extras import RealDictCursor
import os

class UsuarioModel:
    def __init__(self):
        # Configura tu conexión aquí o impórtala de tu archivo de conexión
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )

    # ---------------------------------------------------------
    # 1. CREATE (Crear Usuario)
    # ---------------------------------------------------------
    def crear_usuario(self, nombre, apellido, cedula, contrasena, telefono, direccion, estado="Registrado"):
        """
        Inserta un nuevo usuario incluyendo los campos de contacto y estado.
        """
        sql = """
            INSERT INTO usuarios (nombre, apellido, cedula, contrasena, telefono, direccion, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id, nombre, apellido, estado;
        """
        try:
            cur = self.conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(sql, (nombre, apellido, cedula, contrasena, telefono, direccion, estado))
            nuevo_usuario = cur.fetchone()
            self.conn.commit()
            cur.close()
            return nuevo_usuario
        except Exception as e:
            self.conn.rollback()
            return {"error": str(e)}

    # ---------------------------------------------------------
    # 2. READ (Leer Usuarios)
    # ---------------------------------------------------------
    def obtener_todos(self):
        """Devuelve la lista de todos los usuarios."""
        sql = "SELECT id, nombre, apellido, cedula, telefono, direccion, estado, fecha_creacion FROM usuarios"
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(sql)
        usuarios = cur.fetchall()
        cur.close()
        return usuarios

    def obtener_por_id(self, id_usuario):
        """Busca un usuario específico por su ID."""
        sql = "SELECT * FROM usuarios WHERE id = %s"
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(sql, (id_usuario,))
        usuario = cur.fetchone()
        cur.close()
        return usuario

    # ---------------------------------------------------------
    # 3. UPDATE (Actualizar Usuario)
    # ---------------------------------------------------------
    def actualizar_usuario(self, id_usuario, nombre, apellido, cedula, telefono, direccion, estado):
        """
        Actualiza los datos del usuario. 
        Nota: La contraseña se suele manejar en una función aparte por seguridad, 
        pero si quieres incluirla, agrégala aquí.
        """
        sql = """
            UPDATE usuarios 
            SET nombre = %s, 
                apellido = %s, 
                cedula = %s, 
                telefono = %s, 
                direccion = %s, 
                estado = %s
            WHERE id = %s
            RETURNING id, nombre, apellido, estado;
        """
        try:
            cur = self.conn.cursor(cursor_factory=RealDictCursor)
            datos = (nombre, apellido, cedula, telefono, direccion, estado, id_usuario)
            cur.execute(sql, datos)
            usuario_actualizado = cur.fetchone()
            self.conn.commit()
            cur.close()
            
            if usuario_actualizado is None:
                return {"mensaje": "Usuario no encontrado"}
            return usuario_actualizado
            
        except Exception as e:
            self.conn.rollback()
            return {"error": str(e)}

    # ---------------------------------------------------------
    # 4. DELETE (Eliminar Usuario)
    # ---------------------------------------------------------
    def eliminar_usuario(self, id_usuario):
        """Elimina un usuario por su ID."""
        sql = "DELETE FROM usuarios WHERE id = %s RETURNING id;"
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (id_usuario,))
            eliminado = cur.fetchone()
            self.conn.commit()
            cur.close()
            
            if eliminado:
                return True
            return False
            
        except Exception as e:
            self.conn.rollback()
            return False
            
    def cerrar_conexion(self):
        self.conn.close()