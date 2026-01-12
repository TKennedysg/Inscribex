from dbconexion import get_db_connection


class TipoCupo:
    def __init__(self, nombre_tipo):
        self.__nombre_tipo = nombre_tipo

    # CREATE
    def guardar(self):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tipo_cupo (nombre_tipo)
                VALUES (%s)
                ON CONFLICT (nombre_tipo) DO NOTHING
            """, (self.__nombre_tipo,))
            conn.commit()
            print(f"Tipo de cupo '{self.__nombre_tipo}' registrado")

        except Exception as e:
            conn.rollback()
            print("Error al guardar tipo de cupo:", e)

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
                SELECT id, nombre_tipo
                FROM tipo_cupo
                ORDER BY id
            """)
            tipos = cursor.fetchall()

            print("\nLISTA DE TIPOS DE CUPO:")
            for t in tipos:
                print(f"ID: {t[0]} | Tipo: {t[1]}")

        except Exception as e:
            print("Error al listar tipos de cupo:", e)

        finally:
            cursor.close()
            conn.close()

    # UPDATE
    @staticmethod
    def actualizar(id_tipo, nuevo_nombre):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE tipo_cupo
                SET nombre_tipo = %s
                WHERE id = %s
            """, (nuevo_nombre, id_tipo))
            conn.commit()
            print("Tipo de cupo actualizado correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar tipo de cupo:", e)

        finally:
            cursor.close()
            conn.close()

    # DELETE
    @staticmethod
    def eliminar(id_tipo):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM tipo_cupo WHERE id = %s",
                (id_tipo,)
            )
            conn.commit()
            print("Tipo de cupo eliminado correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar tipo de cupo:", e)

        finally:
            cursor.close()
            conn.close()


# PRUEBA AUTOMÁTICA
if __name__ == "__main__":

    tipos = [
        "Nivelación",
        "Primer semestre"
    ]

    for t in tipos:
        TipoCupo(t).guardar()

    TipoCupo.listar()
