# Imports necesarios
from Aspirante_versioncompleta import AspiranteBuilder
from class_Inscripcion import Inscripcion
from class_Historial import Historial
from class_PeriodoAcademico import Periodo_Academico

if __name__ == "__main__":
    print("=== SISTEMA CON PATRONES BUILDER Y OBSERVER ===\n")

    # 1. USANDO BUILDER para crear el Aspirante
    # Ya no usamos new Aspirante(a,b,c,d,e), usamos pasos lógicos
    print("--- 1. Creando Aspirante con Builder ---")
    builder = AspiranteBuilder()
    aspirante = (builder
                 .con_datos_personales("Maria Gonzalez", "1712345678", "maria@email.com")
                 .con_contacto("0991234567", "Av. Principal 456")
                 .build())
    
    aspirante.registrarse()

    # 2. CONFIGURACIÓN PREVIA
    periodo = Periodo_Academico("2025-1", "Ene", "Jun")
    periodo.abrir_periodo()

    # 3. CREANDO LA INSCRIPCIÓN (SUJETO)
    inscripcion = Inscripcion(aspirante, periodo)

    # 4. CREANDO EL HISTORIAL (OBSERVADOR)
    historial = Historial(aspirante.nombre)

    # 5. CONECTANDO LOS CABLES (OBSERVER)
    # Le decimos a la inscripción: "Cuando cambies, avísale al historial"
    print("\n--- 2. Conectando Observer ---")
    inscripcion.suscribir(historial)

    # 6. PROBANDO LA MAGIA
    print("\n--- 3. Realizando cambios de estado ---")
    
    # Al ejecutar esto, el historial se actualizará SOLO, sin llamarlo explícitamente
    inscripcion.registrarse() 
    
    print("\n...Simulando aprobación administrativa...")
    inscripcion.actualizar_estado("aprobada")

    print("\n...Simulando rechazo por error...")
    inscripcion.actualizar_estado("rechazada")

    # 7. VERIFICAR RESULTADO
    print("\n--- 4. Consultando el Historial Final ---")
    # Verás que tiene todos los eventos registrados automáticamente
    historial.consultar_historial()