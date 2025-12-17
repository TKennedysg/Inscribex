from abc import ABC, abstractmethod

class IUniversidad(ABC):

    @abstractmethod
    def agregar_sede(self, sede):
        pass

    @abstractmethod
    def agregar_carrera(self, carrera):
        pass

    @abstractmethod
    def agregar_jornada(self, jornada):
        pass

    @abstractmethod
    def asignar_oferta_academica(self, oferta):
        pass
