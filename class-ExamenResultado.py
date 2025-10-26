class examenResultado:
    def __init__(self, calificacion, estado, fecha):
        self.calificacion = calificacion
        self.estado = estado
        self.fecha = fecha
    
    def revisarResultado(self):
        if self.calificacion >= 600:
            self.estado = "Aprobado"
        else:
            self.estado = "Reprobado"
        return self.estado
    
    def validarResultado(self):
        if self.estado == "Aprobado":
            print("El examen ha sido aprobado.")
        else:
            print("El examen no ha sido aprobado.")

    def obtenerreporte(self):
        reporte = f"Fecha: {self.fecha}, Calificación: {self.calificacion}, Estado: {self.estado}"
        return reporte
resex = examenResultado(500, "Pendiente", "2025-10-15")
resex.revisarResultado()
resex.obtenerreporte()
resex.validarResultado()