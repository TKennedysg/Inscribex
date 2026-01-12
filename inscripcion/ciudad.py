from dbconexion import get_db_connection


class Ciudad:
    def __init__(self, nombre_ciudad, provincia_id):
        self.__nombre_ciudad = nombre_ciudad
        self.__provincia_id = provincia_id

    # ========================
    # CREATE
    # ========================
    def guardar(self):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            sql = """
                INSERT INTO ciudad (nombre_ciudad, provincia_id)
                VALUES (%s, %s)
            """
            cursor.execute(sql, (self.__nombre_ciudad, self.__provincia_id))
            conn.commit()
            print(f"Ciudad '{self.__nombre_ciudad}' registrada")

        except Exception as e:
            conn.rollback()
            print("Error al guardar ciudad:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # READ
    # ========================
    @staticmethod
    def listar():
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT c.id, c.nombre_ciudad, p.nombre_provincia
                FROM ciudad c
                JOIN provincia p ON c.provincia_id = p.id
                ORDER BY c.id
            """)
            ciudades = cursor.fetchall()

            print("LISTA DE CIUDADES:")
            for c in ciudades:
                print(f"ID: {c[0]} | Ciudad: {c[1]} | Provincia: {c[2]}")

        except Exception as e:
            print("Error al listar ciudades:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # UPDATE
    # ========================
    @staticmethod
    def actualizar(id_ciudad, nuevo_nombre, nueva_provincia_id):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            sql = """
                UPDATE ciudad
                SET nombre_ciudad = %s,
                    provincia_id = %s
                WHERE id = %s
            """
            cursor.execute(sql, (nuevo_nombre, nueva_provincia_id, id_ciudad))
            conn.commit()
            print("Ciudad actualizada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar ciudad:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # DELETE
    # ========================
    @staticmethod
    def eliminar(id_ciudad):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM ciudad WHERE id = %s",
                (id_ciudad,)
            )
            conn.commit()
            print("Ciudad eliminada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar ciudad:", e)

        finally:
            cursor.close()
            conn.close()


# ==================================================
# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
# ==================================================
if __name__ == "__main__":

    # 🔹 Asumimos que las provincias ya existen con estos IDs:
    # Manabí = 1, Pichincha = 2, Guayas = 3, Azuay = 4, Los Ríos = 5
    ciudades = [
        ("Portoviejo", 1),
        ("Manta", 1),
        ("Quito", 2),
        ("Guayaquil", 3),
        ("Cuenca", 4),
        ("Babahoyo", 5)
    ]

    for nombre, provincia_id in ciudades:
        Ciudad(nombre, provincia_id).guardar()

    print("\n--- CIUDADES REGISTRADAS ---")
    Ciudad.listar()
