# Carrera.py
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
        print(f"Jornada: {self.jornada.tipo}")