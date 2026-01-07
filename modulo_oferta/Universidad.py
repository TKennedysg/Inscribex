# Universidad.py
class Universidad:
    def __init__(self, nombre):
        if not nombre:
            raise ValueError("El nombre de la universidad es obligatorio")
        self.nombre = nombre
        self._sedes = []
        self._carreras = []
        self._jornadas = []
        self._oferta_academica = None

    # Métodos para agregar entidades
    def agregar_sede(self, sede):
        self._sedes.append(sede)

    def agregar_carrera(self, carrera):
        self._carreras.append(carrera)

    def agregar_jornada(self, jornada):
        self._jornadas.append(jornada)

    def asignar_oferta_academica(self, oferta):
        self._oferta_academica = oferta

    # Métodos de consulta
    def listar_sedes(self):
        return self._sedes.copy()

    def listar_carreras(self):
        return self._carreras.copy()

    def listar_jornadas(self):
        return self._jornadas.copy()

    # Mostrar info completa
    def mostrar_info(self):
        print("\nUniversidad:", self.nombre)
        print("Sedes:")
        for s in self.listar_sedes():
            print(" -", s.nombre)
        print("Carreras:")
        for c in self.listar_carreras():
            print(" -", c.nombre)
        print("Jornadas:")
        for j in self.listar_jornadas():
            print(" -", j.tipo)