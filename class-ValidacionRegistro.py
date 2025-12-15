from datetime import datetime

class ValidacionRegistro:
    def __init__(self, fecha_validacion=None, resultado="pendiente", observacion=""):
        self.fecha_validacion = fecha_validacion or datetime.now().strftime("%d/%m/%Y")
        self.__resultado = resultado  # pendiente, validado, rechazado
        self.__observacion = observacion
        self.__documentos_requeridos = ["documento_identidad", "certificado_estudios", "foto"]

    # GETTERS para acceso controlado
    @property
    def resultado(self):
        return self.__resultado
    
    @property
    def observacion(self):
        return self.__observacion

    def verificarRegistro(self, documentos_entregados):
        """Verifica si los documentos entregados cumplen con los requerimientos"""
        if not documentos_entregados:
            self.__resultado = "rechazado"
            self.__observacion = "No se entregaron documentos"
            return self.__resultado
        
        # Verificar documentos faltantes
        documentos_faltantes = []
        for doc in self.__documentos_requeridos:
            if doc not in documentos_entregados:
                documentos_faltantes.append(doc)
        
        if documentos_faltantes:
            self.__resultado = "rechazado"
            self.__observacion = f"Documentos faltantes: {', '.join(documentos_faltantes)}"
        else:
            self.__resultado = "validado"
            self.__observacion = "Todos los documentos son válidos y completos"
        
        return self.__resultado

    def verificarDocumentosCompletos(self, documentos_entregados):
        """Versión más detallada de verificación"""
        documentos_validados = {}
        
        for doc in self.__documentos_requeridos:
            if doc in documentos_entregados and documentos_entregados[doc]:
                documentos_validados[doc] = "Válido"
            else:
                documentos_validados[doc] = "Faltante"
        
        return documentos_validados

    def aprobar(self):
        """Aprueba el registro solo si está validado"""
        if self.__resultado == "validado":
            print(f"Registro APROBADO - Observación: {self.__observacion}")
            return True
        else:
            print(f"No se puede aprobar - Estado actual: {self.__resultado}")
            return False

    def rechazar(self, motivo):
        """Rechaza el registro con un motivo específico"""
        self.__resultado = "rechazado"
        self.__observacion = motivo
        print(f"Registro RECHAZADO - Motivo: {motivo}")

    def generarResultado(self):
        """Genera un reporte completo de la validación"""
        return (f"REPORTE DE VALIDACIÓN\n"
                f"Fecha: {self.fecha_validacion}\n"
                f"Resultado: {self.__resultado}\n"
                f"Observación: {self.__observacion}")

    def obtenerEstado(self):
        """Retorna el estado actual de la validación"""
        return self.__resultado

    def reiniciarValidacion(self):
        """Reinicia el proceso de validación"""
        self.__resultado = "pendiente"
        self.__observacion = ""
        print("Validación reiniciada")

# Ejemplo de prueba
if __name__ == "__main__":
    validacion = ValidacionRegistro()
    
    # Simular documentos entregados
    documentos = {
        "documento_identidad": "123456789",
        "certificado_estudios": "certificado.pdf", 
        "foto": "foto.jpg"
    }
    
    print(validacion.verificarRegistro(documentos))
    print(validacion.verificarDocumentosCompletos(documentos))
    validacion.aprobar()
    print(validacion.generarResultado())