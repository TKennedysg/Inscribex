class Universidad:
    def __init__(self, nombre, ubicacion, rector):
        print(f"Universidad {nombre} creada con rector {rector}.")
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.rector = rector

    def asignar_curso(self):
        print(f"La universidad {self.nombre} está asignando cursos a sus facultades.")

    def publicar_oferta(self):
        print(f"La universidad {self.nombre} ha publicado la nueva oferta académica.")

    def recibir_postulaciones(self):
        print(f"La universidad {self.nombre} está recibiendo postulaciones de aspirantes.")
