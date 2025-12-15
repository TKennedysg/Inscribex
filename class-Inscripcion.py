from datetime import datetime

class Inscripcion:
    def __init__(self, aspirante, periodo_academico, id_inscripcion=None, estado="pendiente"):
        self.__aspirante = aspirante
        self.__periodo_academico = periodo_academico
        self.__id_inscripcion = id_inscripcion or f"INS-{aspirante.cedula}-{datetime.now().strftime('%Y%m%d')}"
        self.__fecha = datetime.now().strftime("%d/%m/%Y")
        self.__estado = estado  # pendiente, completada, aprobada, rechazada

    # GETTERS para acceder a los atributos privados
    @property
    def aspirante(self):
        return self.__aspirante
    
    @property
    def id_inscripcion(self):
        return self.__id_inscripcion
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def ingresar_datos(self, datos_aspirante):
        """Ingresa y valida los datos del aspirante"""
        if self.validar_datos(datos_aspirante):
            print("Datos ingresados y validados correctamente")
            return True
        else:
            print("Error en la validación de datos")
            return False

    def validar_datos(self, datos):
        """Valida los datos básicos del aspirante"""
        required_fields = ['nombre', 'cedula', 'correo', 'telefono', 'direccion']
        for field in required_fields:
            if field not in datos or not datos[field]:
                print(f"Campo requerido faltante: {field}")
                return False
        return True

    def registrarse(self):
        """Completa el proceso de registro"""
        print("Iniciando proceso de registro...")
        
        # Verificar que el período esté activo
        if not self.__periodo_academico.verificar_inscripcion_activa():
            print("No se puede registrar - Período académico no activo")
            return False
        
        # Verificar datos básicos del aspirante
        datos_aspirante = {
            'nombre': self.__aspirante.nombre,
            'cedula': self.__aspirante.cedula,
            'correo': self.__aspirante.correo,
            'telefono': self.__aspirante.telefono,
            'direccion': self.__aspirante.direccion
        }
        
        if self.validar_datos(datos_aspirante):
            self.__estado = "completada"
            print(f"Registro completado exitosamente - ID: {self.__id_inscripcion}")
            return True
        else:
            print("Error en el registro - Datos incompletos")
            return False

    def consultar_estado(self):
        """Consulta el estado actual de la inscripción"""
        return f"Inscripción ID: {self.__id_inscripcion} | Estado: {self.__estado} | Fecha: {self.__fecha}"

    def actualizar_estado(self, nuevo_estado):
        """Actualiza el estado de la inscripción"""
        estados_validos = ["pendiente", "completada", "aprobada", "rechazada"]
        if nuevo_estado in estados_validos:
            estado_anterior = self.__estado
            self.__estado = nuevo_estado
            print(f"Estado actualizado: {estado_anterior} → {nuevo_estado}")
            return True
        else:
            print(f"Estado no válido: {nuevo_estado}")
            return False

    def obtener_info_completa(self):
        """Obtiene información completa de la inscripción"""
        return {
            'id_inscripcion': self.__id_inscripcion,
            'aspirante': self.__aspirante.nombre,
            'cedula': self.__aspirante.cedula,
            'periodo': self.__periodo_academico.nombre_periodo,
            'fecha': self.__fecha,
            'estado': self.__estado
        }

# Ejemplo de prueba
if __name__ == "__main__":
    from Aspirante import Aspirante
    from class-PeriodoAcademico import Periodo_Academico
    
    # Crear objetos de prueba
    aspirante = Aspirante("Carlos Ruiz", "0912345678", "carlos@email.com", "0987654321", "Av. Test 123")
    periodo = Periodo_Academico("2025-1", "15-enero-2025", "15-junio-2025")
    periodo.abrir_periodo()
    
    inscripcion = Inscripcion(aspirante, periodo)
    inscripcion.registrarse()
    print(inscripcion.consultar_estado())