from dbconexion import get_db_connection


class DuracionCarrera:
    def __init__(self, nombre_duracion):
        self.__nombre_duracion = nombre_duracion

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
                INSERT INTO duracion_carreras (nombre_duracion)
                VALUES (%s)
            """
            cursor.execute(sql, (self.__nombre_duracion,))
            conn.commit()
            print(f"Duración '{self.__nombre_duracion}' registrada")

        except Exception as e:
            conn.rollback()
            print("Error al guardar duración:", e)

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
            cursor.execute("SELECT id, nombre_duracion FROM duracion_carreras")
            duraciones = cursor.fetchall()

            print("LISTA DE DURACIONES:")
            for d in duraciones:
                print(f"ID: {d[0]} | Duración: {d[1]}")

        except Exception as e:
            print("Error al listar duraciones:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # UPDATE
    # ========================
    @staticmethod
    def actualizar(id_duracion, nuevo_nombre):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            sql = """
                UPDATE duracion_carreras
                SET nombre_duracion = %s
                WHERE id = %s
            """
            cursor.execute(sql, (nuevo_nombre, id_duracion))
            conn.commit()
            print("Duración actualizada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar duración:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # DELETE
    # ========================
    @staticmethod
    def eliminar(id_duracion):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM duracion_carreras WHERE id = %s", (id_duracion,))
            conn.commit()
            print("Duración eliminada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar duración:", e)

        finally:
            cursor.close()
            conn.close()


# ==================================================
# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
# ==================================================
if __name__ == "__main__":

    duraciones = [
        "8",   # 8 semestres
        "10",   # 10 semestres
    ]

    for d in duraciones:
        duracion = DuracionCarrera(d)
        duracion.guardar()

    print("\n--- DURACIONES REGISTRADAS ---")
    DuracionCarrera.listar()
