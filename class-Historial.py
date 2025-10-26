class Historial:
    def __init__ (self, aspirante, fecha_actualizada, estado):
        self.aspirante = aspirante
        self.fecha_actualizada = fecha_actualizada
        self.estado = estado

    def registrar_historial(self):
        return f"Historial registrado para {self.aspirante} el {self.fecha_actualizada} con estado: {self.estado}"
    
    def limpiar_historial(self):
        self.aspirante = None
        self.fecha_actualizada = None
        self.estado = None
        return "Historial limpiado exitosamente."
    
    def consultar_historial(self):
        return f"Aspirante: {self.aspirante}, Fecha Actualizada: {self.fecha_actualizada}, Estado: {self.estado}"
    
    