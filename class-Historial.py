class Historial:
    def __init__ (self, aspirante, fecha_actualizada, estado):
        self.aspirante = aspirante
        self.fecha_actualizada = fecha_actualizada
        self.estado = estado

    def registrar_historial(self):
        print(f"Historial registrado para {self.aspirante} el {self.fecha_actualizada} con estado: {self.estado}")
    
    def consultar_historial(self):
        print (f"Aspirante: {self.aspirante}, Fecha Actualizada: {self.fecha_actualizada}, Estado: {self.estado}")
    
    def limpiar_historial(self):
        self.aspirante = ""
        self.fecha_actualizada = ""
        self.estado = ""
        print("Historial limpiado.")
hist = Historial("Ana Gomez", "2025-10-25", "Activo")
hist.registrar_historial()
hist.consultar_historial()  
hist.limpiar_historial()