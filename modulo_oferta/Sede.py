class Sede:
    def __init__(self, nombre, direccion, cupos_totales):
        self.nombre = nombre
        self.direccion = direccion
        self.cupos_totales = cupos_totales
        self.carreras_disponibles = []

    def agregar_carrera(self, carrera):
        self.carreras_disponibles.append(carrera)

    def mostrar_sede(self):
        print(f"\n Sede: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print("Carreras disponibles:")
        for c in self.carreras_disponibles:
            print(" -", c.nombre)