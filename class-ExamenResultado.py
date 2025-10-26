class examenResultado:
    def __init__(self, calificacion, estado, fecha):
        self.calificacion = calificacion
        self.estado = estado
        self.fecha = fecha
    
    def revisarResultado(self):
        if self.calificacion >= 60:
            self.estado = "Aprobado"
        else:
            self.estado = "Reprobado"
        return self.estado
    
    def validarResultado(self):
        pass

    def obtenerreporte(self):
        reporte = f"Fecha: {self.fecha}, Calificación: {self.calificacion}, Estado: {self.estado}"
        return reporte