class PlanificacionExamen:
    def __init__(self, fecha, aula, monitor):
        self.fecha = fecha
        self.aula = aula
        self.monitor = monitor
        self.participantes = []

    def asignar(self, aspirante):
        self.participantes.append(aspirante)
        return f"Aspirante {aspirante} asignado al examen del {self.fecha} en el aula {self.aula}"

    def modificar(self, nueva_fecha=None, nuevo_aula=None):
        if nueva_fecha:
            self.fecha = nueva_fecha
        if nuevo_aula:
            self.aula = nuevo_aula
        return f"Planificación actualizada: Fecha {self.fecha}, Aula {self.aula}"

    def generarCronograma(self):
        return f"Examen planificado el {self.fecha} en aula {self.aula}, Monitor: {self.monitor}, Participantes: {len(self.participantes)}"