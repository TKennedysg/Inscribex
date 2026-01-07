from Carrera import Carrera
from Sede import Sede

class CarreraFactory:
    @staticmethod
    def crear_carrera(tipo, nombre, duracion, cupos, jornada):
        if tipo == "ingenieria":
            return Carrera(nombre, duracion, cupos, jornada)
        elif tipo == "salud":
            return Carrera(nombre, duracion, cupos, jornada)
        else:
            raise ValueError("Tipo de carrera no válido")

class SedeFactory:
    @staticmethod
    def crear_sede(tipo, nombre, direccion, cupos_totales):
        if tipo in ["matriz", "extension"]:
            return Sede(nombre, direccion, cupos_totales)
        else:
            raise ValueError("Tipo de sede no válido")
        
