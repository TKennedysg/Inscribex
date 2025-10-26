class Examen:
    def __init__(self, area, preguntas, horario, tipo, calificacion):
        self.area = area
        self.preguntas = preguntas
        self.horario = horario
        self.tipo = tipo
        self.calificacion = calificacion

    def realizar_examen(self):
        return f"Realizando un examen de {self.area} con {self.preguntas} preguntas."
    
    def generar_reporte(self):
        return f"El examen de {self.area} fue de tipo {self.tipo} y obtuvo una calificación de {self.calificacion}."
    
    def calificar_examen(self, nueva_calificacion):
        self.calificacion = nueva_calificacion
        return f"La calificación del examen de {self.area} ha sido actualizada a {self.calificacion}."
    
    
