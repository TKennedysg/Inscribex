class OfertaAcademica:
    def __init__(self):
        self.carreras = []
        self.sedes = []
        self.jornadas = []

    def agregar_carrera(self, carrera):
        self.carreras.append(carrera)

    def agregar_sede(self, sede):
        self.sedes.append(sede)

    def agregar_jornada(self, jornada):
        self.jornadas.append(jornada)

    def visualizar(self):
        print("\nOferta Académica Publicada:")
        print("Carreras:")
        for c in self.carreras:
            print(" -", c.nombre)

        print("Sedes:")
        for s in self.sedes:
            print(" -", s.nombre)

        print("Jornadas:")
        for j in self.jornadas:
            print(" -", j.tipo)

    def publicar(self):
        print("\nLa oferta académica ha sido publicada correctamente.")
        self.visualizar()
