class Historial:
    def __init__ (self, aspirante, fecha_actualizada, estado):
        # Atributos Privados
        self.__aspirante = aspirante
        self.__fecha_actualizada = fecha_actualizada
        self.__estado = estado
        
        self.__registrar_historial() 
        
    def __registrar_historial(self):
        print(f"Historial registrado para {self.__aspirante} el {self.__fecha_actualizada} con estado: {self.__estado}")
    
    def consultar_historial(self):
        print (f"Aspirante: {self.__aspirante}, Fecha Actualizada: {self.__fecha_actualizada}, Estado: {self.__estado}")
    
    def limpiar_historial(self):
        self.__aspirante = ""
        self.__fecha_actualizada = ""
        self.__estado = ""
        print("Historial limpiado.")

hist = Historial("Ana Gomez", "2025-10-25", "Activo") 
hist.consultar_historial()
hist.limpiar_historial()