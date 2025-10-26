class PlanificacionExamen:
    def __init__(self, fecha, aula, monitor):
        print(f"Planificación creada para el examen del {fecha} en aula {aula}.")
        self.fecha = fecha
        self.aula = aula
        self.monitor = monitor

    def asignar(self):
        print(f"Asignando monitor {self.monitor} al aula {self.aula} para el examen del {self.fecha}.")

    def modificar(self):
        print(f"Modificando la planificación del examen en aula {self.aula}.")

    def consultar(self):
        print(f"Consulta: examen planificado el {self.fecha} en aula {self.aula}, a cargo de {self.monitor}.")
