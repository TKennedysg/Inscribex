class Examen:
    def __init__(self, area, preguntas, horario, tipo, calificacion):
        self.area = area
        self.preguntas = preguntas
        self.horario = horario
        self.tipo = tipo
        self.calificacion = calificacion

    def realizar_examen(self):
        print(f"Realizando un examen de {self.area} con {self.preguntas} preguntas.")
    
    def generar_reporte(self):
        print(f"El examen de {self.area} fue de tipo {self.tipo} y obtuvo una calificación de {self.calificacion}.")
    
    def calificar_examen(self, nueva_calificacion):
        self.calificacion = nueva_calificacion
        print (f"La calificación del examen de {self.area} ha sido actualizada a {self.calificacion}.")

ex = Examen("Matemáticas, Fisica", 60, "10:00 AM - 25-10-2025 ", "Teórico-Practico", 650)
ex.realizar_examen()
ex.generar_reporte()
ex.calificar_examen(720)
ex.generar_reporte()