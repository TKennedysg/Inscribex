class ValidacionRegistro:
    def __init__(self, fecha_validacion, resultado, observacion):
        self.fecha_validacion = fecha_validacion  
        self.__resultado = resultado            
        self.__observacion = observacion           

    def verificarRegistro(self, estado_documentos):
        if estado_documentos:
            self.__resultado = "Validado"
            self.__observacion = "Documentos validos."
        else:
            self.__resultado = "Rechazado"
            self.__observacion = "Faltan documentos o estan incorrectos."
        return self.__resultado

    def aprobar(self):
        print(f"Registro aprobado. Observacion: {self.__observacion}")

    def generarResultado(self):
        return f"Fecha: {self.fecha_validacion}, Resultado: {self.__resultado}, Observacion: {self.__observacion}"

    def obtenerEstado(self):
        return self.__resultado
    
validacion = ValidacionRegistro(fecha_validacion="25/10/2025", resultado="", observacion="")
print(validacion.verificarRegistro(True))
validacion.aprobar()
print(validacion.generarResultado())
print("Estado actual:", validacion.obtenerEstado())