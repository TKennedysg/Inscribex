class Universidad:
    def __init__(self, nombre, ubicacion, profesores, estudiantes, carrera, malla_curricular):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.profesores = profesores
        self.estudiantes = estudiantes
        self.carrera = carrera
        self.malla_curricular = malla_curricular

    def Asignacion_Cupos(self):
        return f"Se han asignado cupos en la universidad '{self.nombre}' para la carrera {self.carrera}."

    def publicar_oferta(self):
        print(f"La universidad {self.nombre} ha publicado una nueva oferta academica.")

    def recibir_postulaciones(self):
        print(f"La universidad {self.nombre} esta recibiendo postulaciones de aspirantes.")