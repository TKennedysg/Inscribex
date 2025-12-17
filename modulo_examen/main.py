
from Examen import Examen
from ExamenResultado import ExamenResultado
from Proxy_Examen import ProxyExamen
from Proxy_ResultadoExamen import ProxyResultadoExamen

examen = Examen("Matemáticas", 60, "10:00 AM", "Teórico-Práctico", 650)
proxy_examen = ProxyExamen(examen, "estudiante")

proxy_examen.realizar_examen()
proxy_examen.calificar_examen(700)

proxy_docente = ProxyExamen(examen, "docente")
proxy_docente.calificar_examen(700)
proxy_docente.generar_reporte()

resultado = ExamenResultado(700, "Pendiente", "2025-10-15")
proxy_resultado = ProxyResultadoExamen(resultado, "docente")

proxy_resultado.actualizarEstado()
print(proxy_resultado.obtenerreporte())
