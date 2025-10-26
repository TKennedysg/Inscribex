class ValidacionRegistro:
    def __init__(self, fecha_validacion, resultado, observacion):
        self.fecha_validacion = fecha_validacion
        self.resultado = resultado
        self.observacion = observacion

    def verificarRegistro(self, estado_documentos):
        if estado_documentos:
            self.resultado = "Validado"
            self.observacion = "Documentos validos."
        else:
            self.resultado = "Rechazado"
            self.observacion = "Faltan documentos o estan incorrectos."
        return self.resultado

    def aprobar(self):
        print(f"Registro aprobado, su Observacion: {self.observacion}")

    def generarResultado(self):
        return f"Fecha: {self.fecha_validacion}, Resultado: {self.resultado}, Observacion: {self.observacion}"

    def obtenerEstado(self):
        return self.resultado
    
validacion = ValidacionRegistro(fecha_validacion="2025-10-26", resultado="", observacion="")
print(validacion.verificarRegistro(True))
validacion.aprobar()
print(validacion.generarResultado())
print("Estado actual:", validacion.obtenerEstado())