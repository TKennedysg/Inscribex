from abc import ABC, abstractmethod

# Interfaz Observer
class IObservador(ABC):
    @abstractmethod
    def actualizar(self, sujeto, evento_detalle):
        """Método que se ejecuta cuando el sujeto cambia"""
        pass

