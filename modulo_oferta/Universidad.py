class Universidad:
    def __init__(self, nombre: str):
        if not nombre:
            raise ValueError("El nombre de la universidad es obligatorio")

        self.nombre = nombre
        self._sedes = []
        self._carreras = []
        self._jornadas = []
        self._oferta_academica = None

    # Métodos de dominio
    def agregar_sede(self, sede):
        if sede is None:
            raise ValueError("La sede no puede ser nula")
        if sede in self._sedes:
            raise ValueError("La sede ya está registrada")
        self._sedes.append(sede)

    def agregar_carrera(self, carrera):
        if carrera is None:
            raise ValueError("La carrera no puede ser nula")
        if carrera in self._carreras:
            raise ValueError("La carrera ya está registrada")
        self._carreras.append(carrera)

    def agregar_jornada(self, jornada):
        if jornada is None:
            raise ValueError("La jornada no puede ser nula")
        if jornada in self._jornadas:
            raise ValueError("La jornada ya está registrada")
        self._jornadas.append(jornada)

    def asignar_oferta_academica(self, oferta):
        if oferta is None:
            raise ValueError("La oferta académica no puede ser nula")
        self._oferta_academica = oferta

    def obtener_oferta_academica(self):
        if self._oferta_academica is None:
            raise RuntimeError("La universidad no tiene una oferta académica asignada")
        return self._oferta_academica

    # Métodos de consulta
    def listar_sedes(self):
        return self._sedes.copy()

    def listar_carreras(self):
        return self._carreras.copy()

    def listar_jornadas(self):
        return self._jornadas.copy()
    
    # Método para mostrar toda la info de la universidad
    def mostrar_info(self):
        print("\nUniversidad:", self.nombre)

        print("Sedes:")
        for sede in self.listar_sedes():
            print(" -", sede.nombre)

        print("Carreras:")
        for carrera in self.listar_carreras():
            print(" -", carrera.nombre)

        print("Jornadas:")
        for jornada in self.listar_jornadas():
            print(" -", jornada.tipo)