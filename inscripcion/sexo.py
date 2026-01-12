from dbconexion import get_db_connection


class Sexo:
    def __init__(self, nombre_sexo):
        self.__nombre_sexo = nombre_sexo

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
                INSERT INTO sexo (nombre_sexo)
                VALUES (%s)
            """
            cursor.execute(sql, (self.__nombre_sexo,))
            conn.commit()
            print(f"Sexo '{self.__nombre_sexo}' registrado")

        except Exception as e:
            conn.rollback()
            print("Error al guardar sexo:", e)

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
                SELECT id, nombre_sexo
                FROM sexo
                ORDER BY id
            """)
            sexos = cursor.fetchall()

            print("LISTA DE SEXOS:")
            for s in sexos:
                print(f"ID: {s[0]} | Sexo: {s[1]}")

        except Exception as e:
            print("Error al listar sexos:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # UPDATE
    # ========================
    @staticmethod
    def actualizar(id_sexo, nuevo_nombre):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            sql = """
                UPDATE sexo
                SET nombre_sexo = %s
                WHERE id = %s
            """
            cursor.execute(sql, (nuevo_nombre, id_sexo))
            conn.commit()
            print("Sexo actualizado correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar sexo:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # DELETE
    # ========================
    @staticmethod
    def eliminar(id_sexo):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM sexo WHERE id = %s",
                (id_sexo,)
            )
            conn.commit()
            print("Sexo eliminado correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar sexo:", e)

        finally:
            cursor.close()
            conn.close()


# ==================================================
# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
# ==================================================
if __name__ == "__main__":

    sexos = [
        "Masculino",
        "Femenino"
    ]

    for s in sexos:
        Sexo(s).guardar()

    print("\n--- SEXOS REGISTRADOS ---")
    Sexo.listar()
