class PlanificacionExamen:
    def __init__(self, fecha, aula, horarios_disponibles, capacidad, planificacion, cantidad, monitoreo):
        self.__fecha = fecha                        
        self.__aula = aula                          
        self._horarios_disponibles = horarios_disponibles  
        self.__capacidad = capacidad                
        self.planificacion = planificacion         
        self._cantidad = cantidad                   
        self.__monitoreo = monitoreo                
        self.__participantes = []                    

    def Asignar(self, aspirante):
        if len(self.__participantes) < self.__capacidad:
            self.__participantes.append(aspirante)
            return f"Aspirante {aspirante} ha sido asignado al examen del {self.__fecha} en el aula {self.__aula}."
        else:
            return f"No se puede asignar, el aula {self.__aula} alcanzó su capacidad máxima ({self.__capacidad})."
    
    def Organizar(self):
        return f"Examen organizado en {self.__aula} con capacidad de {self.__capacidad} alumnos bajo modalidad '{self.planificacion}'."

    def Generar_Cronograma(self):
        return f"Cronograma generado. Aula: {self.__aula}, Planificación: {self.planificacion}, Monitoreo: {self.__monitoreo}."
    
plan_examen = PlanificacionExamen(
    fecha="10/11/2025",
    aula="A101",
    horarios_disponibles=["08:00-10:00", "10:30-12:30"],
    capacidad=2,
    planificacion="Presencial",
    cantidad=30,
    monitoreo="Supervisor 3"
)
print(plan_examen.Asignar("Pepito Perez"))
print(plan_examen.Asignar("Kennedy Lopez"))
print(plan_examen.Asignar("Chito Vera"))
print(plan_examen.Organizar())
print(plan_examen.Generar_Cronograma())