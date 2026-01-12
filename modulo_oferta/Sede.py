from dbconexion import get_db_connection


class Sede:
    def __init__(self, nombre_sede):
        self.__nombre_sede = nombre_sede

    # CREATE
    def guardar(self):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO sedes (nombre_sede)
                VALUES (%s)
                ON CONFLICT (nombre_sede) DO NOTHING
            """, (self.__nombre_sede,))
            conn.commit()
            print(f"Sede '{self.__nombre_sede}' registrada")

        except Exception as e:
            conn.rollback()
            print("Error al guardar sede:", e)

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
                SELECT id, nombre_sede
                FROM sedes
                ORDER BY id
            """)
            sedes = cursor.fetchall()

            print("\nLISTA DE SEDES:")
            for s in sedes:
                print(f"ID: {s[0]} | Sede: {s[1]}")

        except Exception as e:
            print("Error al listar sedes:", e)

        finally:
            cursor.close()
            conn.close()

    # UPDATE
    @staticmethod
    def actualizar(id_sede, nuevo_nombre):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE sedes
                SET nombre_sede = %s
                WHERE id = %s
            """, (nuevo_nombre, id_sede))
            conn.commit()
            print("Sede actualizada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar sede:", e)

        finally:
            cursor.close()
            conn.close()

    # DELETE
    @staticmethod
    def eliminar(id_sede):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM sedes WHERE id = %s",
                (id_sede,)
            )
            conn.commit()
            print("Sede eliminada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar sede:", e)

        finally:
            cursor.close()
            conn.close()


# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
if __name__ == "__main__":

    sedes = [
        "Matriz Manta",
        "Extensión Chone",
        "Extensión Sucre",
        "Extensión El Carmen",
        "Extensión Pedernales",
        "Campus Pichinca",
        "Campus Flavio Alfaro",
        "Sede Santo Domingo",
        "Campus Tosagua",
        "Santa Ana",
        "Junín",
        "San Isidro",
        "Puerto López"
    ]

    for s in sedes:
        Sede(s).guardar()

    Sede.listar()
