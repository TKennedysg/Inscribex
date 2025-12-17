from typing import List
from modulo_oferta.interfaces.Universidad import IUniversidad

class Universidad(IUniversidad):
    """
    Entidad de dominio principal (Aggregate Root)
    Representa a la Universidad dentro del sistema
    """

    def __init__(self, nombre: str):
        if not nombre:
            raise ValueError("El nombre de la universidad es obligatorio")

        self._nombre = nombre
        self._sedes: List = []
        self._carreras: List = []
        self._jornadas: List = []
        self._oferta_academica = None

    # =========================
    # Métodos de dominio
    # =========================

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

    # =========================
    # Inyección de dependencias
    # =========================

    def asignar_oferta_academica(self, oferta):
        if oferta is None:
            raise ValueError("La oferta académica no puede ser nula")
        self._oferta_academica = oferta

    def obtener_oferta_academica(self):
        if self._oferta_academica is None:
            raise RuntimeError("La universidad no tiene una oferta académica asignada")
        return self._oferta_academica

    # =========================
    # Métodos de consulta
    # =========================

    @property
    def nombre(self):
        return self._nombre

    def listar_sedes(self):
        return self._sedes.copy()

    def listar_carreras(self):
        return self._carreras.copy()

    def listar_jornadas(self):
        return self._jornadas.copy()
