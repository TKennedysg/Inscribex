class Universidad:
    def __init__(self, nombre, ubicacion, profesores, estudiantes, carrera, malla_curricular):
        self.nombre = nombre                      
        self.ubicacion = ubicacion                
        self._profesores = profesores             
        self._estudiantes = estudiantes           
        self.carrera = carrera                    
        self._malla_curricular = malla_curricular 

    def Asignacion_Cupos(self):
        return f"Se han asignado cupos en la universidad '{self.nombre}' para la carrera {self.carrera}."

    def publicar_oferta(self):
        print(f"La universidad {self.nombre} ha publicado una nueva oferta academica.")

    def recibir_postulaciones(self):
        print(f"La universidad {self.nombre} esta recibiendo postulaciones de aspirantes.")

    def mostrar_malla(self):
        print(f"Malla curricular de {self.carrera}:")
        for materia in self._malla_curricular:
            print("-", materia)

uni = Universidad(
    nombre="Universidad Laica Eloy Alfaro de Manabí",
    ubicacion="Manta",
    profesores=["Prof. Jarol", "Prof. Ener Valencia"],
    estudiantes=["Pepito", "Pinocho"],
    carrera="Ingeniería de Software",
    malla_curricular=["Álgebra Lineal", "Programación Orientada a Objetos", "Modelado Orientado a Objetos"]
)
print(uni.Asignacion_Cupos())
uni.publicar_oferta()
uni.recibir_postulaciones()
uni.mostrar_malla()
<<<<<<< HEAD


=======
>>>>>>> 91af998e4ec945f3550a4e286a7e658da9b54dc7
