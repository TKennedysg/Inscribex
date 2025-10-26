class PlanificacionExamen:
    def __init__(self, fecha, aula, horarios_disponibles, capacidad, planificacion, cantidad, monitoreo):
        self.fecha = fecha
        self.aula = aula
        self.horarios_disponibles = horarios_disponibles
        self.capacidad = capacidad
        self.planificacion = planificacion
        self.cantidad = cantidad
        self.monitoreo = monitoreo
        self.participantes = []

    def Asignar(self, aspirante):
        if len(self.participantes) < self.capacidad:
            self.participantes.append(aspirante)
            return f"Aspirante {aspirante} ha sido asignado al examen del {self.fecha} en el aula {self.aula}."
        else:
            return f"No se puede asignar, el Aula {self.aula} ha alcanzado su capacidad maxima ({self.capacidad}) de personas."
    
    def Organizar(self):
        return f"Examen organizado en {self.aula} con capacidad de {self.capacidad} alumnos bajo modalidad '{self.planificacion}'."

    def Generar_Cronograma(self):
        return f"Cronograma generado. Aula: {self.aula}, Planificación: {self.planificacion}, Monitoreo: {self.monitoreo}."
    
plan_examen = PlanificacionExamen(
    fecha="2025-11-10",
    aula="A101",
    horarios_disponibles=["08:00-10:00", "10:30-12:30"],
    capacidad=2,
    planificacion="Presencial",
    cantidad=30,
    monitoreo="Supervisor 1"
)
print(plan_examen.Asignar("Juan Perez"))
print(plan_examen.Asignar("Ana Mendoza"))
print(plan_examen.Asignar("Carlos Vera"))
print(plan_examen.Organizar())
print(plan_examen.Generar_Cronograma())