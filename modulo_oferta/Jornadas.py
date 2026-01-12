from dbconexion import get_db_connection


class Jornada:
    def __init__(self, nombre_jornada):
        self.__nombre_jornada = nombre_jornada

    # CREATE
    def guardar(self):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            sql = """
                INSERT INTO jornadas_academicas (nombre_jornada)
                VALUES (%s)
                ON CONFLICT (nombre_jornada) DO NOTHING
            """
            cursor.execute(sql, (self.__nombre_jornada,))
            conn.commit()
            print(f"Jornada '{self.__nombre_jornada}' registrada")

        except Exception as e:
            conn.rollback()
            print("Error al guardar jornada:", e)

        finally:
            cursor.close()
            conn.close()

    # READ
    @staticmethod
    def listar():
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, nombre_jornada
                FROM jornadas_academicas
                ORDER BY id
            """)
            jornadas = cursor.fetchall()

            print("\nLISTA DE JORNADAS:")
            for j in jornadas:
                print(f"ID: {j[0]} | Jornada: {j[1]}")

        except Exception as e:
            print("Error al listar jornadas:", e)

        finally:
            cursor.close()
            conn.close()

    # UPDATE
    @staticmethod
    def actualizar(id_jornada, nuevo_nombre):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            sql = """
                UPDATE jornadas_academicas
                SET nombre_jornada = %s
                WHERE id = %s
            """
            cursor.execute(sql, (nuevo_nombre, id_jornada))
            conn.commit()
            print("Jornada actualizada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar jornada:", e)

        finally:
            cursor.close()
            conn.close()

    # DELETE
    @staticmethod
    def eliminar(id_jornada):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM jornadas_academicas WHERE id = %s",
                (id_jornada,)
            )
            conn.commit()
            print("Jornada eliminada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar jornada:", e)

        finally:
            cursor.close()
            conn.close()


# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
if __name__ == "__main__":

    jornadas = [
        "Matutina",
        "Vespertina",
        "Nocturna"
    ]

    for j in jornadas:
        Jornada(j).guardar()

    Jornada.listar()
