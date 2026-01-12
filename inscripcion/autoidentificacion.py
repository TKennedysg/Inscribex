from dbconexion import get_db_connection


class AutoIdentificacion:
    def __init__(self, nombre_autoidentificacion):
        self.__nombre_autoidentificacion = nombre_autoidentificacion

    # ========================
    # CREATE
    # ========================
    def guardar(self):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO autoidentificacion (nombre_autoidentificacion)
                VALUES (%s)
                ON CONFLICT (nombre_autoidentificacion) DO NOTHING
            """, (self.__nombre_autoidentificacion,))
            conn.commit()
            print(f"Autoidentificación '{self.__nombre_autoidentificacion}' registrada (si no existía)")

        except Exception as e:
            conn.rollback()
            print("Error al guardar autoidentificación:", e)

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
                SELECT id, nombre_autoidentificacion
                FROM autoidentificacion
                ORDER BY id
            """)
            registros = cursor.fetchall()

            print("LISTA DE AUTOIDENTIFICACIONES:")
            for r in registros:
                print(f"ID: {r[0]} | Autoidentificación: {r[1]}")

        except Exception as e:
            print("Error al listar autoidentificaciones:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # UPDATE
    # ========================
    @staticmethod
    def actualizar(id_auto, nuevo_nombre):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE autoidentificacion
                SET nombre_autoidentificacion = %s
                WHERE id = %s
            """, (nuevo_nombre, id_auto))
            conn.commit()
            print("Autoidentificación actualizada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar autoidentificación:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # DELETE
    # ========================
    @staticmethod
    def eliminar(id_auto):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM autoidentificacion WHERE id = %s",
                (id_auto,)
            )
            conn.commit()
            print("Autoidentificación eliminada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar autoidentificación:", e)

        finally:
            cursor.close()
            conn.close()


# ==================================================
# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
# ==================================================
if __name__ == "__main__":

    autoidentificaciones = [
        "Cédula de identidad",
        "Pasaporte"
    ]

    for nombre in autoidentificaciones:
        AutoIdentificacion(nombre).guardar()

    print("\n--- AUTOIDENTIFICACIONES REGISTRADAS ---")
    AutoIdentificacion.listar()
