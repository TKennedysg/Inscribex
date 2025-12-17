from Inscribex.modulo_oferta.Carrera import Carrera

class CarreraFactory:

    def crear_carrera(self, tipo, nombre, duracion, cupos, jornada):
        if tipo == "ingenieria":
            return Carrera(nombre, duracion, cupos, jornada)

        elif tipo == "salud":
            return Carrera(nombre, duracion, cupos, jornada)

        else:
            raise ValueError("Tipo de carrera no válido")