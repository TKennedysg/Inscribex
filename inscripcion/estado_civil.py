from dbconexion import get_db_connection


class EstadoCivil:
    def __init__(self, nombre_estado_civil):
        self.__nombre_estado_civil = nombre_estado_civil

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
                INSERT INTO estado_civil (nombre_estado_civil)
                VALUES (%s)
            """
            cursor.execute(sql, (self.__nombre_estado_civil,))
            conn.commit()
            print(f"Estado civil '{self.__nombre_estado_civil}' registrado")

        except Exception as e:
            conn.rollback()
            print("Error al guardar estado civil:", e)

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
                SELECT id, nombre_estado_civil
                FROM estado_civil
                ORDER BY id
            """)
            estados = cursor.fetchall()

            print("LISTA DE ESTADOS CIVILES:")
            for e in estados:
                print(f"ID: {e[0]} | Estado civil: {e[1]}")

        except Exception as e:
            print("Error al listar estados civiles:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # UPDATE
    # ========================
    @staticmethod
    def actualizar(id_estado_civil, nuevo_nombre):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            sql = """
                UPDATE estado_civil
                SET nombre_estado_civil = %s
                WHERE id = %s
            """
            cursor.execute(sql, (nuevo_nombre, id_estado_civil))
            conn.commit()
            print("Estado civil actualizado correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar estado civil:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # DELETE
    # ========================
    @staticmethod
    def eliminar(id_estado_civil):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM estado_civil WHERE id = %s",
                (id_estado_civil,)
            )
            conn.commit()
            print("Estado civil eliminado correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar estado civil:", e)

        finally:
            cursor.close()
            conn.close()


# ==================================================
# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
# ==================================================
if __name__ == "__main__":

    estados_civiles = [
        "Soltero",
        "Casado",
        "Divorciado",
        "Viudo",
        "Unión libre"
    ]

    for e in estados_civiles:
        EstadoCivil(e).guardar()

    print("\n--- ESTADOS CIVILES REGISTRADOS ---")
    EstadoCivil.listar()
