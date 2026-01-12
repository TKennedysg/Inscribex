from dbconexion import get_db_connection


class Sala:
    def __init__(self, nombre_sala):
        self.__nombre_sala = nombre_sala

    # CREATE
    def guardar(self):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO sala (nombre_sala)
                VALUES (%s)
                ON CONFLICT (nombre_sala) DO NOTHING
            """, (self.__nombre_sala,))
            conn.commit()
            print(f"Sala '{self.__nombre_sala}' registrada")

        except Exception as e:
            conn.rollback()
            print("Error al guardar sala:", e)

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
                SELECT id, nombre_sala
                FROM sala
                ORDER BY id
            """)
            salas = cursor.fetchall()

            print("\nLISTA DE SALAS:")
            for s in salas:
                print(f"ID: {s[0]} | Sala: {s[1]}")

        except Exception as e:
            print("Error al listar salas:", e)

        finally:
            cursor.close()
            conn.close()

    # UPDATE
    @staticmethod
    def actualizar(id_sala, nuevo_nombre):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE sala
                SET nombre_sala = %s
                WHERE id = %s
            """, (nuevo_nombre, id_sala))
            conn.commit()
            print("Sala actualizada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar sala:", e)

        finally:
            cursor.close()
            conn.close()

    # DELETE
    @staticmethod
    def eliminar(id_sala):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM sala WHERE id = %s",
                (id_sala,)
            )
            conn.commit()
            print("Sala eliminada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar sala:", e)

        finally:
            cursor.close()
            conn.close()


# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
if __name__ == "__main__":

    salas = [
        "Sala 101",
        "Sala 102",
        "Sala 206",
        "Sala 104",
        "Sala 203",
        "Sala 306"
    ]

    for s in salas:
        Sala(s).guardar()

    Sala.listar()
