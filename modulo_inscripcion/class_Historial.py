from datetime import datetime
from Interfaces import IObservador

class Historial(IObservador):
    def __init__(self, aspirante, fecha_actualizada=None, estado="creado"):
        # Atributos Privados
        self.__aspirante = aspirante
        self.__fecha_actualizada = fecha_actualizada or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__estado = estado
        self.__eventos = []  # Lista para mantener múltiples eventos
        
        # Llamamos al método interno
        self.__registrar_historial() 
        
    # --- MÉTODO RECUPERADO QUE FALTABA ---
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
    
    # --- IMPLEMENTACIÓN DEL PATRÓN OBSERVER ---
    def actualizar(self, sujeto, evento_detalle):
        """Método que recibe la notificación automática"""
        nuevo_estado = sujeto.estado
        print(f"👀 OBSERVADOR NOTIFICADO: El historial detectó cambio -> {evento_detalle}")
        # Registramos el evento automáticamente
        self.agregar_evento("actualizacion_automatica", nuevo_estado, evento_detalle)

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
        return f"🔄 Aspirante: {self.__aspirante} | Estado: {self.__estado} | Última actualización: {self.__fecha_actualizada}"