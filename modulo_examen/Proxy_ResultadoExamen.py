
class ProxyResultadoExamen:
    def __init__(self, resultado_real, rol_usuario):
        self._resultado_real = resultado_real
        self._rol_usuario = rol_usuario  # docente, estudiante

    def actualizarEstado(self):
        if self._rol_usuario == "docente":
            return self._resultado_real.actualizarEstado()
        else:
            print("No tiene permisos para actualizar el estado")
            return None

    def validarResultado(self):
        if self._rol_usuario in ["docente", "estudiante"]:
            self._resultado_real.validarResultado()
        else:
            print("Acceso denegado")

    def obtenerreporte(self):
        if self._rol_usuario == "docente":
            return self._resultado_real.obtenerreporte()
        else:
            return "Reporte no disponible"
