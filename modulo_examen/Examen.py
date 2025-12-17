class Examen:
    def __init__(self, area, preguntas, horario, tipo, calificacion):
        self.area = area
        self._preguntas = preguntas
        self.__horario = horario
        self._tipo = tipo
        self.__calificacion = calificacion

    def realizar_examen(self):
        print(f"Realizando un examen de {self.area} con {self._preguntas} preguntas.")
    
    def generar_reporte(self):
        print(f"El examen de {self.area} fue de tipo {self._tipo} y obtuvo una calificación de {self.__calificacion}.")
    
    def calificar_examen(self, nueva_calificacion):
        self.calificacion = nueva_calificacion
        print (f"La calificación del examen de {self.area} ha sido actualizada a {self.__calificacion}.")

ex = Examen("Matemáticas, Fisica", 60, "10:00 AM - 25-10-2025 ", "Teórico-Practico", 650)
ex.realizar_examen()
ex.generar_reporte()
ex.calificar_examen(720)
ex.generar_reporte()