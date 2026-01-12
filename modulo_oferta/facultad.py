from dbconexion import get_db_connection


class Facultad:
    def __init__(self, nombre_facultad, abreviacion):
        self.__nombre_facultad = nombre_facultad
        self.__abreviacion = abreviacion

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
                INSERT INTO facultades (nombre_facultad, abreviacion)
                VALUES (%s, %s)
            """
            cursor.execute(sql, (self.__nombre_facultad, self.__abreviacion))
            conn.commit()
            print(f"Facultad '{self.__abreviacion}' registrada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al guardar facultad:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # READ (listar)
    # ========================
    @staticmethod
    def listar():
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre_facultad FROM facultades")
            facultades = cursor.fetchall()

            print("LISTA DE FACULTADES:")
            for f in facultades:
                print(f"ID: {f[0]} | Nombre: {f[1]}")

        except Exception as e:
            print("Error al listar facultades:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # UPDATE
    # ========================
    @staticmethod
    def actualizar(id_facultad, nuevo_nombre, nueva_abreviacion):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            sql = """
                UPDATE facultades
                SET nombre_facultad = %s, abreviacion = %s
                WHERE id = %s
            """
            cursor.execute(sql, (nuevo_nombre, nueva_abreviacion, id_facultad))
            conn.commit()
            print("Facultad actualizada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al actualizar facultad:", e)

        finally:
            cursor.close()
            conn.close()

    # ========================
    # DELETE
    # ========================
    @staticmethod
    def eliminar(id_facultad):
        conn = get_db_connection()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM facultades WHERE id = %s", (id_facultad,))
            conn.commit()
            print("Facultad eliminada correctamente")

        except Exception as e:
            conn.rollback()
            print("Error al eliminar facultad:", e)

        finally:
            cursor.close()
            conn.close()


# ==================================================
# PRUEBA AUTOMÁTICA AL EJECUTAR EL ARCHIVO
# ==================================================
if __name__ == "__main__":

    # facultades = [
    #     ("Facultad Ciencias de la Salud", "FCS"),
    #     ("Facultad Ciencias Administrativas, Contables y Comercio", "FCACC"),
    #     ("Facultad de Educación Turismo y Humanidades", "FETH"),
    #     ("Facultad Ingeniería, Industria y Arquitectura", "FIIA"),
    #     ("Facultad de Ciencias de la Vida y la Tecnología", "FCVT"),
    #     ("Facultad de Ciencias Sociales, Derecho y Bienestar", "FCSDB"),
    #     ("Facultad de Artes", "FA"),
    #     ("Unidad de Formación Técnicas y Tecnológicas", "UFTT"),
    # ]

    # for nombre, abreviacion in facultades:
    #     facultad = Facultad(nombre, abreviacion)
    #     facultad.guardar()



    print("\n--- CONSULTA DESPUÉS DE INSERTAR ---")
    Facultad.listar()

    # # INSERTAR 2 FACULTADES DE EJEMPLO
    # facultad1 = Facultad("Facultad de Ciencias de la Salud")
    # facultad2 = Facultad("Facultad de Ingeniería y Tecnología")

    # facultad1.guardar()
    # facultad2.guardar()

    # print("\n--- CONSULTA DESPUÉS DE INSERTAR ---")
    # Facultad.listar()


    # print("\n--- LISTA ANTES DE EDITAR ---")
    # Facultad.listar()

    # # EDITAR FACULTAD CON ID = 1
    # Facultad.actualizar(
    #     id_facultad=1,
    #     nuevo_nombre="Facultad de Ciencias Médicas"
    # )

    # print("\n--- LISTA DESPUÉS DE EDITAR ---")
    # Facultad.listar()




# #CREACIÓN DE FACULTADES 
# fcs = Facultad("Facultad Ciencias de la Salud")
# fcacc = Facultad("Facultad Ciencias Administrativas, Contables y Comercio")
# feth = Facultad("Facultad de Educación Turismo y Humanidades")
# fiia = Facultad("Facultad Ingeniería, Industria y Arquitectura")
# fcvt = Facultad("Facultad de Ciencias de la Vida y la Tecnología")
# fcsdb = Facultad("Facultad de Ciencias Sociales, Derecho y Bienestar")
# fa = Facultad("Facultad de Artes")
# uftt = Facultad("Unidad de Formación Técnicas y Tecnológicas")


# #CARRERAS POR FACULTAD 

# # Ciencias de la Salud
# fcs.agregar_carrera(Carrera("Enfermería", "Matutina"))
# fcs.agregar_carrera(Carrera("Fisioterapia", "Vespertina"))
# fcs.agregar_carrera(Carrera("Laboratorio clínico", "jornada2"))
# fcs.agregar_carrera(Carrera("Laboratorio clínico", "jornada2"))
# fcs.agregar_carrera(Carrera("Medicina", "Vespertina"))
# fcs.agregar_carrera(Carrera("Nutrición", "Vespertina"))
# fcs.agregar_carrera(Carrera("Odontología", "Vespertina"))
# fcs.agregar_carrera(Carrera("Terapia ocupacional", "Vespertina"))


# # Ciencias Administrativas
# fcacc.agregar_carrera(Carrera("Administración de Empresas", "Matutina"))
# fcacc.agregar_carrera(Carrera("Auditoría y control de gestión", "Matutina"))
# fcacc.agregar_carrera(Carrera("Comercio exterior", "Vespertina"))
# fcacc.agregar_carrera(Carrera("Contabilidad y Auditoría", "Vespertina"))
# fcacc.agregar_carrera(Carrera("Gestión de talento humano", "Vespertina"))
# fcacc.agregar_carrera(Carrera("Gestión de la informacion gerencial", "Vespertina"))
# fcacc.agregar_carrera(Carrera("Finanzas", "Vespertina"))
# fcacc.agregar_carrera(Carrera("Mercadotecnia", "Vespertina"))

# # Educación, Turismo y Humanidades
# feth.agregar_carrera(Carrera("Educación Inicial", "Matutina"))
# feth.agregar_carrera(Carrera("Educación Básica", "Vespertina"))
# feth.agregar_carrera(Carrera("Educación básica bilingüe", "Matutina"))
# feth.agregar_carrera(Carrera("Educación inclusiva", "Matutina"))
# feth.agregar_carrera(Carrera("Entrenamiento deportivo", "Matutina"))
# feth.agregar_carrera(Carrera("Gestión hotelera internacional", "Matutina"))
# feth.agregar_carrera(Carrera("Pedagogía de la Lengua y la Literatura", "Matutina"))
# feth.agregar_carrera(Carrera("Pedagogía de los Idiomas Nacionales y Extranjeros", "Vespertina"))
# feth.agregar_carrera(Carrera("Pedagogía de la Actividad Física y el Deporte", "Vespertina"))
# feth.agregar_carrera(Carrera("Psicología educativa", "Vespertina"))
# feth.agregar_carrera(Carrera("Turismo sostenible", "Vespertina"))

# # Ingeniería, Industria y Arquitectura
# fiia.agregar_carrera(Carrera("Arquitectura", "Matutina"))
# fiia.agregar_carrera(Carrera("Electricidad", "Matutina"))
# fiia.agregar_carrera(Carrera("Electricidad", "Matutina"))
# fiia.agregar_carrera(Carrera("Ingeniería Civil", "Vespertina"))
# fiia.agregar_carrera(Carrera("Ingeniería Civil", "Vespertina"))
# fiia.agregar_carrera(Carrera("Ingeniería Industrial", "Vespertina"))
# fiia.agregar_carrera(Carrera("Ingeniería Industrial", "Vespertina"))
# fiia.agregar_carrera(Carrera("Ingeniería Marítima", "Vespertina"))
# fiia.agregar_carrera(Carrera("Ingeniería Marítima", "Vespertina"))

# # Ciencias de la Vida y Tecnología
# fcvt.agregar_carrera(Carrera("Agroindustria", "Matutina"))
# fcvt.agregar_carrera(Carrera("Agronegocios", "Matutina"))
# fcvt.agregar_carrera(Carrera("Agropecuaria", "Matutina"))
# fcvt.agregar_carrera(Carrera("Alimentos", "Matutina"))
# fcvt.agregar_carrera(Carrera("Biología", "Vespertina"))
# fcvt.agregar_carrera(Carrera("Ingeniería Ambiental", "Vespertina"))
# fcvt.agregar_carrera(Carrera("Software", "Vespertina"))
# fcvt.agregar_carrera(Carrera("Tecnología de la Información", "Vespertina"))

# # Ciencias Sociales, Derecho y Bienestar
# fcsdb.agregar_carrera(Carrera("Comunicaión", "Vespertina"))
# fcsdb.agregar_carrera(Carrera("Ciencias Políticas y Relaciones Internacionales", "Vespertina"))
# fcsdb.agregar_carrera(Carrera("Criminología y Ciencias Forenses", "Vespertina"))
# fcsdb.agregar_carrera(Carrera("Derecho", "Vespertina"))
# fcsdb.agregar_carrera(Carrera("Derecho", "Vespertina"))
# fcsdb.agregar_carrera(Carrera("Economía", "Vespertina"))
# fcsdb.agregar_carrera(Carrera("Gestión Pública y Desarrollo", "Vespertina"))
# fcsdb.agregar_carrera(Carrera("Trabajo Social", "Vespertina"))

# # Artes
# fa.agregar_carrera(Carrera("Arqueología", "Vespertina"))
# fa.agregar_carrera(Carrera("Artes Escénicas", "Vespertina"))
# fa.agregar_carrera(Carrera("Artes plasticas", "Vespertina"))
# fa.agregar_carrera(Carrera("Diseño Textil e Indumentaria", "Vespertina"))
# fa.agregar_carrera(Carrera("Sociología", "Vespertina"))

# # Técnicas y Tecnológicas
# uftt.agregar_carrera(Carrera("Bienes raíces", "Vespertina"))
# uftt.agregar_carrera(Carrera("Construcción Sismo Resistente", "Vespertina"))
# uftt.agregar_carrera(Carrera("Gastronomía", "Vespertina"))
# uftt.agregar_carrera(Carrera("Gastronomía", "Vespertina"))
# uftt.agregar_carrera(Carrera("Metalmecánica", "Vespertina"))
# uftt.agregar_carrera(Carrera("Comunicación para Televisión, Relaciones Publicas y Protocolo", "Vespertina"))

# #MOSTRAR FACULTADES Y CARRERAS
# facultades = [fcs, fcacc, feth, fiia, fcvt, fcsdb, fa, uftt]

# for facultad in facultades:
#     facultad.mostrar()