
class ProxyExamen:
    def __init__(self, examen_real, rol_usuario):
        self._examen_real = examen_real
        self._rol_usuario = rol_usuario

    def realizar_examen(self):
        self._examen_real.realizar_examen()

    def calificar_examen(self, nueva_calificacion):
        if self._rol_usuario == "docente":
            self._examen_real.calificar_examen(nueva_calificacion)
        else:
            print("Solo el docente puede calificar el examen")

    def generar_reporte(self):
        if self._rol_usuario in ["docente", "administrativo"]:
            self._examen_real.generar_reporte()
        else:
            print("No tiene permisos para ver el reporte")
