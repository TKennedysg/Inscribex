from dbconexion import get_db_connection


class Nacionalidad:
    def __init__(self, nombre_nacionalidad):
        self.__nombre_nacionalidad = nombre_nacionalidad

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
                INSERT INTO nacionalidad (nombre_nacionalidad)
                VALUES (%s)
            """
            cursor.execute(sql, (self.__nombre_nacionalidad,))
            conn.commit()
            print(f"Nacionalidad '{self.__nombre_nacionalidad}' registrada")

        except Exception as e:
            conn.rollback()
            print("Error al guardar nacionalidad:", e)

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
                SELECT id, nombre_nacionalidad
                FROM nacionalidad
                ORDER BY id
            """)
            nacionalidades = cursor.fetchall()

            print("LISTA DE NACIONALIDADES:")
            for n in nacionalidades:
                print(f"ID: {n[0]} | Nacionalidad: {n[1]}")

        except Exception as e:
            print("Error al listar nacionalidades:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # UPDATE
    # ========================
    @staticmethod
    def actualizar(id_nacionalidad, nuevo_nombre):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            sql = """
                UPDATE nacionalidad
                SET nombre_nacionalidad = %s
                WHERE id = %s
            """
            cursor.execute(sql, (nuevo_nombre, id_nacionalidad))
            conn.commit()
            print("Nacionalidad actualizada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar nacionalidad:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # DELETE
    # ========================
    @staticmethod
    def eliminar(id_nacionalidad):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM nacionalidad WHERE id = %s",
                (id_nacionalidad,)
            )
            conn.commit()
            print("Nacionalidad eliminada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar nacionalidad:", e)

        finally:
            cursor.close()
            conn.close()


# ==================================================
# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
# ==================================================
if __name__ == "__main__":

    nacionalidades = [
        "Ecuatoriana",
        "Colombiana",
        "Venezolana"
    ]

    for n in nacionalidades:
        Nacionalidad(n).guardar()

    print("\n--- NACIONALIDADES REGISTRADAS ---")
    Nacionalidad.listar()
