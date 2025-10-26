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

uni = Universidad(
    nombre="Universidad Laica Eloy Alfaro de Manabi",
    ubicacion="Manta",
    profesores=["Prof. Jarol", "Prof. Ener Valencia"],
    estudiantes=["Pepito", "Pinocho"],
    carrera="Ingenieria de Software",
    malla_curricular=["Algebra Lineal", "Programacion Orientada a Objetos", "Modelado Orientado a OBjetos"]
)
print(uni.Asignacion_Cupos())
uni.publicar_oferta()
uni.recibir_postulaciones()