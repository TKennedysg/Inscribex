class ExamenResultado:
    def __init__(self, calificacion, estado, fecha):
        self.__calificacion = calificacion
        self.__estado = estado
        self._fecha = fecha
    
    def __revisarResultado(self):
        if self.__calificacion >= 600:
            self.__estado = "Aprobado"
        else:
            self.__estado = "Reprobado"
        return self.__estado
    def actualizarEstado(self):
        return self.__revisarResultado()
    
    def validarResultado(self):
        if self.__estado == "Aprobado":
            print("El examen ha sido aprobado.")
        else:
            print("El examen no ha sido aprobado.")

    def obtenerreporte(self):
        reporte = f"Fecha: {self._fecha}, Calificación: {self.__calificacion}, Estado: {self.__estado}"
        return reporte
resex = ExamenResultado(600, "Pendiente", "2025-10-15")
resex.actualizarEstado()
print(resex.obtenerreporte())
resex.validarResultado()