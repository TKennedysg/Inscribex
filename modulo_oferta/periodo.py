from dbconexion import get_db_connection


class Periodo:
    def __init__(self, nombre_periodo):
        self.__nombre_periodo = nombre_periodo

    # CREATE
    def guardar(self):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO periodos (nombre_periodo)
                VALUES (%s)
                ON CONFLICT (nombre_periodo) DO NOTHING
            """, (self.__nombre_periodo,))
            conn.commit()
            print(f"Periodo '{self.__nombre_periodo}' registrado")

        except Exception as e:
            conn.rollback()
            print("Error al guardar periodo:", e)

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
                SELECT id, nombre_periodo
                FROM periodos
                ORDER BY id
            """)
            periodos = cursor.fetchall()

            print("\nLISTA DE PERIODOS:")
            for p in periodos:
                print(f"ID: {p[0]} | Periodo: {p[1]}")

        except Exception as e:
            print("Error al listar periodos:", e)

        finally:
            cursor.close()
            conn.close()

    # UPDATE
    @staticmethod
    def actualizar(id_periodo, nuevo_nombre):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE periodos
                SET nombre_periodo = %s
                WHERE id = %s
            """, (nuevo_nombre, id_periodo))
            conn.commit()
            print("Periodo actualizado correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar periodo:", e)

        finally:
            cursor.close()
            conn.close()

    # DELETE
    @staticmethod
    def eliminar(id_periodo):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM periodos WHERE id = %s",
                (id_periodo,)
            )
            conn.commit()
            print("Periodo eliminado correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar periodo:", e)

        finally:
            cursor.close()
            conn.close()


# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
if __name__ == "__main__":

    periodos = [
        "2025-2",
        "2026-1"
    ]

    for p in periodos:
        Periodo(p).guardar()

    Periodo.listar()
