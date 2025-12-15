from datetime import datetime

class Periodo_Academico:
    def __init__(self, nombre_periodo, fecha_inicio, fecha_final, estado="planificado"):
        self._nombre_periodo = nombre_periodo
        self._fecha_inicio = fecha_inicio
        self._fecha_final = fecha_final
        self._estado = estado  # planificado, abierto, cerrado
        self.__inscripciones = []
        
        print(f"Período académico '{nombre_periodo}' creado: {fecha_inicio} a {fecha_final} - Estado: {estado}")

    # GETTERS para acceso controlado
    @property
    def estado(self):
        return self._estado
    
    @property
    def nombre_periodo(self):
        return self._nombre_periodo

    def abrir_periodo(self):
        """Abre el período para inscripciones"""
        if self._estado == "cerrado":
            print("No se puede reabrir un período cerrado")
            return False
        
        self._estado = "abierto"
        print(f"Período {self._nombre_periodo} ABIERTO para inscripciones")
        return True

    def cerrar_periodo(self, confirmacion=True):
        """Cierra el período académico"""
        if not confirmacion:
            print("Cierre cancelado")
            return False
        
        self._estado = "cerrado"
        print(f"Período {self._nombre_periodo} CERRADO")
        return True

    def consultar_periodo(self):
        """Consulta la información del período"""
        info = f"""
 INFORMACIÓN DEL PERÍODO ACADÉMICO
   Nombre: {self._nombre_periodo}
   Inicio: {self._fecha_inicio}
   Finalización: {self._fecha_final}
   Estado: {self._estado}
   Inscripciones: {len(self.__inscripciones)}
"""
        print(info)
        return info

    def agregar_inscripcion(self, inscripcion):
        """Agrega una inscripción al período"""
        if self._estado != "abierto":
            print(f"No se pueden agregar inscripciones. Período {self._estado}")
            return False
        
        self.__inscripciones.append(inscripcion)
        print(f"Inscripción agregada al período {self._nombre_periodo}")
        return True

    def verificar_inscripcion_activa(self):
        """Verifica si el período acepta inscripciones"""
        return self._estado == "abierto"

    def obtener_estadisticas(self):
        """Obtiene estadísticas del período"""
        return {
            'periodo': self._nombre_periodo,
            'estado': self._estado,
            'total_inscripciones': len(self.__inscripciones),
            'fecha_inicio': self._fecha_inicio,
            'fecha_fin': self._fecha_final
        }

# Ejemplo de prueba
if __name__ == "__main__":
    periodo = Periodo_Academico("2025-2", "15-septiembre", "7-febrero", "planificado")
    periodo.abrir_periodo()
    periodo.consultar_periodo()
    print(f"¿Acepta inscripciones?: {periodo.verificar_inscripcion_activa()}")