from dbconexion import get_db_connection


class Modalidad:
    def __init__(self, nombre):
        self.__nombre = nombre

    # CREATE
    def guardar(self):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO modalidad (nombre)
                VALUES (%s)
                ON CONFLICT (nombre) DO NOTHING
            """, (self.__nombre,))
            conn.commit()
            print(f"Modalidad '{self.__nombre}' registrada")

        except Exception as e:
            conn.rollback()
            print("Error al guardar modalidad:", e)

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
                SELECT id, nombre
                FROM modalidad
                ORDER BY id
            """)
            modalidades = cursor.fetchall()

            print("\nLISTA DE MODALIDADES:")
            for m in modalidades:
                print(f"ID: {m[0]} | Modalidad: {m[1]}")

        except Exception as e:
            print("Error al listar modalidades:", e)

        finally:
            cursor.close()
            conn.close()

    # UPDATE
    @staticmethod
    def actualizar(id_modalidad, nuevo_nombre):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE modalidad
                SET nombre = %s
                WHERE id = %s
            """, (nuevo_nombre, id_modalidad))
            conn.commit()
            print("Modalidad actualizada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar modalidad:", e)

        finally:
            cursor.close()
            conn.close()

    # DELETE
    @staticmethod
    def eliminar(id_modalidad):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM modalidad WHERE id = %s",
                (id_modalidad,)
            )
            conn.commit()
            print("Modalidad eliminada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar modalidad:", e)

        finally:
            cursor.close()
            conn.close()


# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
if __name__ == "__main__":

    modalidades = [
        "Presencial",
        "Semipresencial",
        "Híbrida"
    ]

    for m in modalidades:
        Modalidad(m).guardar()

    Modalidad.listar()
