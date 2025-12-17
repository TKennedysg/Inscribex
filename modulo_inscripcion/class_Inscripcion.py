from datetime import datetime

class Inscripcion:
    def __init__(self, aspirante, periodo_academico):
        self.__aspirante = aspirante
        self.__periodo_academico = periodo_academico
        self.__id_inscripcion = f"INS-{aspirante.cedula}"
        self.__estado = "pendiente"
        
        # LISTA DE SUSCRIPTORES (Patrón Observer)
        self._observadores = []

    # MÉTODOS DEL SUJETO (OBSERVER)
    def suscribir(self, observador):
        self._observadores.append(observador)

    def desuscribir(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self, detalle):
        for obs in self._observadores:
            # A cada observador le decimos: "Hey, yo (self) cambié, mira el detalle"
            obs.actualizar(self, detalle)

    # ... (Getters existentes) ...
    @property
    def estado(self): return self.__estado

    # MODIFICAMOS ESTE MÉTODO PARA QUE AVISE
    def actualizar_estado(self, nuevo_estado):
        estado_anterior = self.__estado
        self.__estado = nuevo_estado
        
        # ¡AQUI ESTA LA MAGIA!
        # Avisamos al historial automáticamente
        self.notificar_observadores(f"Cambio de estado: {estado_anterior} -> {nuevo_estado}")
        
        return True

    # ... (Resto de métodos existentes: registrarse, etc.) ...
    def registrarse(self):
        # Lógica de registro...
        self.__estado = "completada"
        self.notificar_observadores("Inscripción completada inicialmente")