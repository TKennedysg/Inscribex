from dbconexion import get_db_connection


class TipoUnidadEducativa:
    def __init__(self, nombre_tipo):
        self.__nombre_tipo = nombre_tipo

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
                INSERT INTO tipo_unidad_educativa (nombre_tipo)
                VALUES (%s)
            """
            cursor.execute(sql, (self.__nombre_tipo,))
            conn.commit()
            print(f"Tipo de unidad educativa '{self.__nombre_tipo}' registrado")

        except Exception as e:
            conn.rollback()
            print("Error al guardar tipo de unidad educativa:", e)

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
                SELECT id, nombre_tipo
                FROM tipo_unidad_educativa
                ORDER BY id
            """)
            tipos = cursor.fetchall()

            print("LISTA DE TIPOS DE UNIDAD EDUCATIVA:")
            for t in tipos:
                print(f"ID: {t[0]} | Tipo: {t[1]}")

        except Exception as e:
            print("Error al listar tipos de unidad educativa:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # UPDATE
    # ========================
    @staticmethod
    def actualizar(id_tipo, nuevo_nombre):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            sql = """
                UPDATE tipo_unidad_educativa
                SET nombre_tipo = %s
                WHERE id = %s
            """
            cursor.execute(sql, (nuevo_nombre, id_tipo))
            conn.commit()
            print("Tipo de unidad educativa actualizado correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar tipo de unidad educativa:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # DELETE
    # ========================
    @staticmethod
    def eliminar(id_tipo):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM tipo_unidad_educativa WHERE id = %s",
                (id_tipo,)
            )
            conn.commit()
            print("Tipo de unidad educativa eliminado correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar tipo de unidad educativa:", e)

        finally:
            cursor.close()
            conn.close()


# ==================================================
# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
# ==================================================
if __name__ == "__main__":

    tipos = [
        "Fiscal",
        "Fiscomisional",
        "Particular"
    ]

    for t in tipos:
        TipoUnidadEducativa(t).guardar()

    print("\n--- TIPOS DE UNIDAD EDUCATIVA REGISTRADOS ---")
    TipoUnidadEducativa.listar()
