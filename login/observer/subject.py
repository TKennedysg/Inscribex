from abc import ABC, abstractmethod

class Subject(ABC):

    @abstractmethod
    def agregar_observer(self, observer):
        pass

    @abstractmethod
    def quitar_observer(self, observer):
        pass

    @abstractmethod
    def notificar(self, mensaje):
        pass
