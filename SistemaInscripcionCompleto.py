from datetime import datetime
from Aspirante import Aspirante
from Periodo_Academico import Periodo_Academico
from ValidacionRegistro import ValidacionRegistro
from Inscripcion import Inscripcion
from Registro import Registro
from Historial import Historial

class SistemaInscripcionCompleto:
    def __init__(self):
        self.periodo_actual = None
        self.inscripciones = []
        self.historiales = {}
        self.registros = {}
        self.validaciones = {}
    
    def configurar_periodo(self, nombre, fecha_inicio, fecha_fin):
        """Configura el período académico actual"""
        self.periodo_actual = Periodo_Academico(nombre, fecha_inicio, fecha_fin)
        self.periodo_actual.abrir_periodo()
        return self.periodo_actual
    
    def proceso_inscripcion_completo(self, datos_aspirante):
        print("\n" + "="*60)
        print("INICIANDO PROCESO DE INSCRIPCIÓN COMPLETO")
        print("="*60)
        
        # 1. VERIFICAR PERÍODO ACTIVO
        if not self.periodo_actual or not self.periodo_actual.verificar_inscripcion_activa():
            print("No hay período académico activo para inscripciones")
            return False
        
        # 2. CREAR ASPIRANTE
        try:
            aspirante = Aspirante(
                datos_aspirante['nombre'],
                datos_aspirante['cedula'],
                datos_aspirante['correo'],
                datos_aspirante['telefono'],
                datos_aspirante['direccion']
            )
            print("Aspirante creado exitosamente")
        except KeyError as e:
            print(f"Faltan datos requeridos: {e}")
            return False
        
        # 3. REGISTRAR ASPIRANTE
        aspirante.registrarse()
        
        # 4. AGREGAR DOCUMENTOS
        for doc_type, doc_file in datos_aspirante.get('documentos', {}).items():
            aspirante.agregar_documento(doc_type, doc_file)
        
        # 5. CREAR INSCRIPCIÓN
        inscripcion = Inscripcion(aspirante, self.periodo_actual)
        inscripcion.registrarse()
        
        # 6. VALIDAR DOCUMENTOS
        validacion = ValidacionRegistro()
        documentos_entregados = aspirante.obtener_documentos()
        resultado_validacion = validacion.verificarRegistro(list(documentos_entregados.keys()))
        
        if resultado_validacion == "validado":
            # 7. CREAR REGISTRO OFICIAL
            registro = Registro(inscripcion.id_inscripcion, aspirante)
            registro.registrar()
            registro.actualizarEstado("completado")
            
            # 8. AGREGAR AL PERÍODO
            self.periodo_actual.agregar_inscripcion(inscripcion)
            
            # 9. ACTUALIZAR ESTADOS
            aspirante.estado = "inscrito"
            inscripcion.estado = "aprobada"
            
            # 10. CREAR HISTORIAL
            historial = Historial(aspirante.nombre)
            historial.agregar_evento("inscripcion_iniciada", "en_proceso", "Proceso de inscripción iniciado")
            historial.agregar_evento("documentos_entregados", "documentos_verificados", "Todos los documentos entregados")
            historial.agregar_evento("validacion_aprobada", "inscrito", "Inscripción aprobada exitosamente")
            
            # GUARDAR EN SISTEMA
            self.inscripciones.append(inscripcion)
            self.historiales[aspirante.cedula] = historial
            self.registros[inscripcion.id_inscripcion] = registro
            self.validaciones[aspirante.cedula] = validacion
            
            print("\n¡PROCESO DE INSCRIPCIÓN COMPLETADO EXITOSAMENTE!")
            print("=" * 50)
            print(f"Aspirante: {aspirante.nombre}")
            print(f"Período: {self.periodo_actual.nombre_periodo}")
            print(f"ID Inscripción: {inscripcion.id_inscripcion}")
            print(f"Estado: {aspirante.estado}")
            print(f"Validación: {validacion.generarResultado()}")
            
            return {
                'success': True,
                'aspirante': aspirante,
                'inscripcion': inscripcion,
                'registro': registro,
                'validacion': validacion,
                'historial': historial
            }
        else:
            print("\nINSCRIPCIÓN RECHAZADA")
            print("=" * 30)
            historial = Historial(aspirante.nombre)
            historial.agregar_evento("inscripcion_rechazada", "rechazado", validacion.observacion)
            print(f"Motivo: {validacion.observacion}")
            
            return {
                'success': False,
                'reason': validacion.observacion,
                'historial': historial
            }
    
    def consultar_estadisticas(self):
        """Muestra estadísticas del sistema"""
        print("\nESTADÍSTICAS DEL SISTEMA")
        print("=" * 30)
        print(f"Período activo: {self.periodo_actual.nombre_periodo if self.periodo_actual else 'Ninguno'}")
        print(f"Total inscripciones: {len(self.inscripciones)}")
        print(f"Total historiales: {len(self.historiales)}")
        print(f"Total registros: {len(self.registros)}")
        
        if self.inscripciones:
            aprobadas = sum(1 for ins in self.inscripciones if ins.estado == "aprobada")
            print(f"Inscripciones aprobadas: {aprobadas}")
            print(f"Inscripciones rechazadas: {len(self.inscripciones) - aprobadas}")

# Ejemplo de uso COMPLETO
if __name__ == "__main__":
    sistema = SistemaInscripcionCompleto()
    
    # Configurar período
    sistema.configurar_periodo("2025-1", "15-enero-2025", "15-junio-2025")
    
    # Datos del aspirante
    datos_aspirante = {
        'nombre': "Maria Gonzalez",
        'cedula': "1712345678", 
        'correo': "maria.gonzalez@email.com",
        'telefono': "0991234567",
        'direccion': "Av. Principal 456",
        'documentos': {
            'documento_identidad': 'cedula_maria.pdf',
            'certificado_estudios': 'certificado_maria.pdf',
            'foto': 'foto_maria.jpg'
        }
    }
    
    # Ejecutar proceso completo
    resultado = sistema.proceso_inscripcion_completo(datos_aspirante)
    
    if resultado['success']:
        print(f"\nCONSULTA DE ESTADO:")
        print(resultado['aspirante'].consultar_estado())
        print(f"\nINFORMACIÓN DE INSCRIPCIÓN:")
        print(resultado['inscripcion'].consultar_estado())
        print(f"\nDATOS DE REGISTRO:")
        resultado['registro'].mostrarDatos()
        print(f"\nHISTORIAL:")
        resultado['historial'].consultar_historial()
    
    # Mostrar estadísticas
    sistema.consultar_estadisticas()