from dbconexion import get_db_connection


class Bloque:
    def __init__(self, nombre_bloque):
        self.__nombre_bloque = nombre_bloque

    # CREATE
    def guardar(self):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO bloque (nombre_bloque)
                VALUES (%s)
                ON CONFLICT (nombre_bloque) DO NOTHING
            """, (self.__nombre_bloque,))
            conn.commit()
            print(f"Bloque '{self.__nombre_bloque}' registrado")

        except Exception as e:
            conn.rollback()
            print("Error al guardar bloque:", e)

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
                SELECT id, nombre_bloque
                FROM bloque
                ORDER BY id
            """)
            bloques = cursor.fetchall()

            print("\nLISTA DE BLOQUES:")
            for b in bloques:
                print(f"ID: {b[0]} | Bloque: {b[1]}")

        except Exception as e:
            print("Error al listar bloques:", e)

        finally:
            cursor.close()
            conn.close()

    # UPDATE
    @staticmethod
    def actualizar(id_bloque, nuevo_nombre):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE bloque
                SET nombre_bloque = %s
                WHERE id = %s
            """, (nuevo_nombre, id_bloque))
            conn.commit()
            print("Bloque actualizado correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar bloque:", e)

        finally:
            cursor.close()
            conn.close()

    # DELETE
    @staticmethod
    def eliminar(id_bloque):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM bloque WHERE id = %s",
                (id_bloque,)
            )
            conn.commit()
            print("Bloque eliminado correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar bloque:", e)

        finally:
            cursor.close()
            conn.close()


# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
if __name__ == "__main__":

    bloques = [
        "Bloque 1",
        "Bloque 2",
        "Bloque 3",
        "Bloque 4",
        "Bloque 5",
        "Bloque 6"
    ]

    for b in bloques:
        Bloque(b).guardar()

    Bloque.listar()
