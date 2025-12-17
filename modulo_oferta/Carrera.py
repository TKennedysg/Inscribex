class Carrera:
    def __init__(self, nombre, duracion, cupos, jornada):
        self.nombre = nombre
        self.duracion = duracion
        self.cupos = cupos
        self.jornada = jornada

    def mostrar_carrera(self):
        print(f"\nCarrera: {self.nombre}")
        print(f"Duración: {self.duracion} años")
        print(f"Cupos: {self.cupos}")
        print(f"Jornada: {self.jornada}")

    def editar(self, nuevo_nombre=None, nueva_duracion=None, nuevos_cupos=None):
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nueva_duracion:
            self.duracion = nueva_duracion
        if nuevos_cupos:
            self.cupos = nuevos_cupos