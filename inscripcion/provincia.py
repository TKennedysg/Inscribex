from dbconexion import get_db_connection


class Provincia:
    def __init__(self, nombre_provincia, pais_id):
        self.__nombre_provincia = nombre_provincia
        self.__pais_id = pais_id

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
                INSERT INTO provincia (nombre_provincia, pais_id)
                VALUES (%s, %s)
            """
            cursor.execute(sql, (self.__nombre_provincia, self.__pais_id))
            conn.commit()
            print(f"Provincia '{self.__nombre_provincia}' registrada")

        except Exception as e:
            conn.rollback()
            print("Error al guardar provincia:", e)

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
                SELECT p.id, p.nombre_provincia, pa.nombre_pais
                FROM provincia p
                JOIN pais pa ON p.pais_id = pa.id
                ORDER BY p.id
            """)
            provincias = cursor.fetchall()

            print("LISTA DE PROVINCIAS:")
            for p in provincias:
                print(f"ID: {p[0]} | Provincia: {p[1]} | País: {p[2]}")

        except Exception as e:
            print("Error al listar provincias:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # UPDATE
    # ========================
    @staticmethod
    def actualizar(id_provincia, nuevo_nombre, nuevo_pais_id):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            sql = """
                UPDATE provincia
                SET nombre_provincia = %s,
                    pais_id = %s
                WHERE id = %s
            """
            cursor.execute(sql, (nuevo_nombre, nuevo_pais_id, id_provincia))
            conn.commit()
            print("Provincia actualizada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar provincia:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # DELETE
    # ========================
    @staticmethod
    def eliminar(id_provincia):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM provincia WHERE id = %s",
                (id_provincia,)
            )
            conn.commit()
            print("Provincia eliminada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar provincia:", e)

        finally:
            cursor.close()
            conn.close()


# ==================================================
# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
# ==================================================
if __name__ == "__main__":

    # 🔹 Asumimos que Ecuador tiene id = 1
    provincias = [
        ("Manabí", 1),
        ("Pichincha", 1),
        ("Guayas", 1),
        ("Azuay", 1),
        ("Los Ríos", 1)
    ]

    for nombre, pais_id in provincias:
        Provincia(nombre, pais_id).guardar()

    print("\n--- PROVINCIAS REGISTRADAS ---")
    Provincia.listar()
