from dbconexion import get_db_connection


class Pais:
    def __init__(self, nombre_pais):
        self.__nombre_pais = nombre_pais

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
                INSERT INTO pais (nombre_pais)
                VALUES (%s)
                ON CONFLICT (nombre_pais) DO NOTHING
            """, (self.__nombre_pais,))
            conn.commit()
            print(f"País '{self.__nombre_pais}' registrado (si no existía)")

        except Exception as e:
            conn.rollback()
            print("Error al guardar país:", e)

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
                SELECT id, nombre_pais
                FROM pais
                ORDER BY id
            """)
            paises = cursor.fetchall()

            print("LISTA DE PAÍSES:")
            for p in paises:
                print(f"ID: {p[0]} | País: {p[1]}")

        except Exception as e:
            print("Error al listar países:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # UPDATE
    # ========================
    @staticmethod
    def actualizar(id_pais, nuevo_nombre):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE pais
                SET nombre_pais = %s
                WHERE id = %s
            """, (nuevo_nombre, id_pais))
            conn.commit()
            print("País actualizado correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar país:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # DELETE
    # ========================
    @staticmethod
    def eliminar(id_pais):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM pais WHERE id = %s",
                (id_pais,)
            )
            conn.commit()
            print("País eliminado correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar país:", e)

        finally:
            cursor.close()
            conn.close()


# ==================================================
# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
# ==================================================
if __name__ == "__main__":

    paises = [
        "Ecuador",
        "Colombia",
        "Venezuela"
    ]

    for nombre in paises:
        Pais(nombre).guardar()

    print("\n--- PAÍSES REGISTRADOS ---")
    Pais.listar()
