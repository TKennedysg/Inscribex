from database import ConexionDB  # Importamos tu nuevo archivo

class Sede:
    def __init__(self, nombre, direccion, ciudad):
        self.nombre = nombre          
        self._direccion = direccion   
        self.ciudad = ciudad          
        self.__activa = True
        # Preparamos la conexión
        self.db = ConexionDB()

    def asignar(self):
        print(f"Asignando recursos a {self.nombre}...")

    def registrar(self):
        """Este método ahora guarda REALMENTE en PostgreSQL"""
        print(f"📡 Intentando registrar sede {self.nombre} en la BD...")
        
        self.db.conectar()
        
        # Sentencia SQL para insertar
        sql = """
        INSERT INTO sedes (nombre, direccion, ciudad, activa) 
        VALUES (%s, %s, %s, %s);
        """
        
        try:
            # Ejecutamos la orden
            self.db.cursor.execute(sql, (self.nombre, self._direccion, self.ciudad, self.__activa))
            self.db.connection.commit() # ¡Guardar cambios!
            print(f"✅ Sede '{self.nombre}' guardada exitosamente en PostgreSQL.")
            
        except Exception as e:
            print(f"❌ Error al guardar: {e}")
            self.db.connection.rollback() # Deshacer si falla
            
        finally:
            self.db.cerrar()

    def obtenerDatos(self):
        return f"Sede: {self.nombre}, Ciudad: {self.ciudad}"

# --- PRUEBA AUTOMÁTICA ---
if __name__ == "__main__":
    # Creamos un objeto Sede
    mi_sede = Sede("Sede Manta Centro", "Av. 4 de Noviembre", "Manta")
    
    # Al ejecutar esto, debería aparecer en tu pgAdmin
    mi_sede.registrar()