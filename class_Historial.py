from datetime import datetime

class Historial:
    def __init__(self, aspirante, fecha_actualizada=None, estado="creado"):
        # Atributos Privados
        self.__aspirante = aspirante
        self.__fecha_actualizada = fecha_actualizada or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__estado = estado
        self.__eventos = []  # Lista para mantener múltiples eventos
        
        self.__registrar_historial() 
        
    def __registrar_historial(self):
        """Registro automático al crear el historial"""
        evento = {
            'fecha': self.__fecha_actualizada,
            'accion': 'creacion_historial',
            'estado': self.__estado,
            'aspirante': self.__aspirante
        }
        self.__eventos.append(evento)
        print(f"📝 Historial creado para {self.__aspirante} - {self.__fecha_actualizada} - Estado: {self.__estado}")
    
    def agregar_evento(self, accion, nuevo_estado=None, observacion=""):
        """Agrega un nuevo evento al historial"""
        fecha_evento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        evento = {
            'fecha': fecha_evento,
            'accion': accion,
            'estado': nuevo_estado or self.__estado,
            'observacion': observacion,
            'aspirante': self.__aspirante
        }
        self.__eventos.append(evento)
        
        if nuevo_estado:
            self.__estado = nuevo_estado
            self.__fecha_actualizada = fecha_evento
        
        print(f"📝 Evento registrado: {accion} - Estado: {nuevo_estado or self.__estado}")
        return evento
    
    def consultar_historial(self):
        """Consulta todo el historial de eventos"""
        print(f"\n📋 HISTORIAL COMPLETO - Aspirante: {self.__aspirante}")
        print("=" * 50)
        for i, evento in enumerate(self.__eventos, 1):
            print(f"{i}. Fecha: {evento['fecha']}")
            print(f"   Acción: {evento['accion']}")
            print(f"   Estado: {evento['estado']}")
            if evento.get('observacion'):
                print(f"   Observación: {evento['observacion']}")
            print("-" * 30)
    
    def consultar_estado_actual(self):
        """Consulta solo el estado actual"""
        return f"🔄 Aspirante: {self.__aspirante} | Estado: {self.__estado} | Última actualización: {self.__fecha_actualizada}"
    
    def obtener_ultimo_evento(self):
        """Obtiene el último evento registrado"""
        if self.__eventos:
            return self.__eventos[-1]
        return None
    
    def limpiar_historial(self):
        """Limpia el historial (con confirmación)"""
        confirmacion = input("¿Está seguro de limpiar el historial? (s/n): ")
        if confirmacion.lower() == 's':
            self.__aspirante = ""
            self.__fecha_actualizada = ""
            self.__estado = ""
            self.__eventos = []
            print("🗑️ Historial limpiado completamente.")
        else:
            print("❌ Operación cancelada.")
    
    def exportar_historial(self):
        """Exporta el historial en formato legible"""
        if not self.__eventos:
            return "No hay eventos en el historial"
        
        reporte = f"REPORTE DE HISTORIAL - Aspirante: {self.__aspirante}\n"
        reporte += "=" * 50 + "\n"
        
        for evento in self.__eventos:
            reporte += f"Fecha: {evento['fecha']} | Acción: {evento['accion']} | Estado: {evento['estado']}\n"
            if evento.get('observacion'):
                reporte += f"Observación: {evento['observacion']}\n"
            reporte += "-" * 30 + "\n"
        
        return reporte

# Ejemplo de prueba
if __name__ == "__main__":
    hist = Historial("Ana Gomez", estado="Activo")
    hist.agregar_evento("inscripcion", "inscrito", "Documentos entregados")
    hist.agregar_evento("validacion", "validado", "Documentos aprobados")
    hist.agregar_evento("pago", "completado", "Matrícula pagada")
    
    hist.consultar_historial()
    print(hist.consultar_estado_actual())
    print("\nÚltimo evento:", hist.obtener_ultimo_evento())