from dbconexion import get_db_connection


class Carrera:
    def __init__(self, nombre_carrera, id_facultad, id_duracion_carrera):
        self.__nombre_carrera = nombre_carrera
        self.__id_facultad = id_facultad
        self.__id_duracion_carrera = id_duracion_carrera

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
                INSERT INTO carreras (nombre_carrera, id_facultad, id_duracion_carrera)
                VALUES (%s, %s, %s)
                ON CONFLICT (nombre_carrera) DO NOTHING
            """
            cursor.execute(
                sql,
                (self.__nombre_carrera, self.__id_facultad, self.__id_duracion_carrera)
            )
            conn.commit()
            print(f"Carrera registrada: {self.__nombre_carrera}")

        except Exception as e:
            conn.rollback()
            print("Error al guardar carrera:", e)

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
                SELECT c.id, c.nombre_carrera, f.nombre_facultad, d.nombre_duracion
                FROM carreras c
                JOIN facultades f ON c.id_facultad = f.id
                JOIN duracion_carreras d ON c.id_duracion_carrera = d.id
                ORDER BY f.id
            """)
            carreras = cursor.fetchall()

            print("\nLISTA DE CARRERAS:")
            for c in carreras:
                print(f"ID: {c[0]} | {c[1]} | {c[2]} | Duración: {c[3]}")

        except Exception as e:
            print("Error al listar carreras:", e)

        finally:
            cursor.close()
            conn.close()


# ==================================================
# CARGA AUTOMÁTICA DE CARRERAS
# ==================================================
if __name__ == "__main__":

    # IDs de duración
    DURACION_SALUD = 2   # 10
    DURACION_GENERAL = 1  # 8

    carreras = [
        # =========================
        # Facultad Ciencias de la Salud (ID 1)
        # =========================
        ("Enfermería", 1, DURACION_SALUD),
        ("Fisioterapia", 1, DURACION_SALUD),
        ("Laboratorio clínico", 1, DURACION_SALUD),
        ("Medicina", 1, DURACION_SALUD),
        ("Nutrición", 1, DURACION_SALUD),
        ("Odontología", 1, DURACION_SALUD),
        ("Terapia ocupacional", 1, DURACION_SALUD),

        # =========================
        # Ciencias Administrativas (ID 2)
        # =========================
        ("Administración de Empresas", 2, DURACION_GENERAL),
        ("Auditoría y control de gestión", 2, DURACION_GENERAL),
        ("Comercio exterior", 2, DURACION_GENERAL),
        ("Contabilidad y Auditoría", 2, DURACION_GENERAL),
        ("Gestión de talento humano", 2, DURACION_GENERAL),
        ("Gestión de la informacion gerencial", 2, DURACION_GENERAL),
        ("Finanzas", 2, DURACION_GENERAL),
        ("Mercadotecnia", 2, DURACION_GENERAL),

        # =========================
        # Educación, Turismo y Humanidades (ID 3)
        # =========================
        ("Educación Inicial", 3, DURACION_GENERAL),
        ("Educación Básica", 3, DURACION_GENERAL),
        ("Educación básica bilingüe", 3, DURACION_GENERAL),
        ("Educación inclusiva", 3, DURACION_GENERAL),
        ("Entrenamiento deportivo", 3, DURACION_GENERAL),
        ("Gestión hotelera internacional", 3, DURACION_GENERAL),
        ("Pedagogía de la Lengua y la Literatura", 3, DURACION_GENERAL),
        ("Pedagogía de los Idiomas Nacionales y Extranjeros", 3, DURACION_GENERAL),
        ("Pedagogía de la Actividad Física y el Deporte", 3, DURACION_GENERAL),
        ("Psicología educativa", 3, DURACION_GENERAL),
        ("Turismo sostenible", 3, DURACION_GENERAL),

        # =========================
        # Ingeniería, Industria y Arquitectura (ID 4)
        # =========================
        ("Arquitectura", 4, DURACION_GENERAL),
        ("Electricidad", 4, DURACION_GENERAL),
        ("Ingeniería Civil", 4, DURACION_GENERAL),
        ("Ingeniería Industrial", 4, DURACION_GENERAL),
        ("Ingeniería Marítima", 4, DURACION_GENERAL),

        # =========================
        # Ciencias de la Vida y Tecnología (ID 5)
        # =========================
        ("Agroindustria", 5, DURACION_GENERAL),
        ("Agronegocios", 5, DURACION_GENERAL),
        ("Agropecuaria", 5, DURACION_GENERAL),
        ("Alimentos", 5, DURACION_GENERAL),
        ("Biología", 5, DURACION_GENERAL),
        ("Ingeniería Ambiental", 5, DURACION_GENERAL),
        ("Software", 5, DURACION_GENERAL),
        ("Tecnología de la Información", 5, DURACION_GENERAL),

        # =========================
        # Ciencias Sociales, Derecho y Bienestar (ID 6)
        # =========================
        ("Comunicación", 6, DURACION_GENERAL),
        ("Ciencias Políticas y Relaciones Internacionales", 6, DURACION_GENERAL),
        ("Criminología y Ciencias Forenses", 6, DURACION_GENERAL),
        ("Derecho", 6, DURACION_GENERAL),
        ("Economía", 6, DURACION_GENERAL),
        ("Gestión Pública y Desarrollo", 6, DURACION_GENERAL),
        ("Trabajo Social", 6, DURACION_GENERAL),

        # =========================
        # Artes (ID 7)
        # =========================
        ("Arqueología", 7, DURACION_GENERAL),
        ("Artes Escénicas", 7, DURACION_GENERAL),
        ("Artes plasticas", 7, DURACION_GENERAL),
        ("Diseño Textil e Indumentaria", 7, DURACION_GENERAL),
        ("Sociología", 7, DURACION_GENERAL),

        # =========================
        # Técnicas y Tecnológicas (ID 8)
        # =========================
        ("Bienes raíces", 8, DURACION_GENERAL),
        ("Construcción Sismo Resistente", 8, DURACION_GENERAL),
        ("Gastronomía", 8, DURACION_GENERAL),
        ("Metalmecánica", 8, DURACION_GENERAL),
        ("Comunicación para Televisión, Relaciones Publicas y Protocolo", 8, DURACION_GENERAL),
    ]

    for nombre, id_facultad, id_duracion in carreras:
        Carrera(nombre, id_facultad, id_duracion).guardar()

    Carrera.listar()
