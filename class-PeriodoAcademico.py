class Periodo_Academico:
    def __init__(self,fecha_inicio,fecha_final,estado):
        print(f"El periodo creado inicia {fecha_inicio} y termina el {fecha_final} ,su estado actual es {estado}")
        self._fecha_inicio=fecha_inicio
        self._fecha_final=fecha_final
        self._estado=estado

    def abrir_periodo(self,periodo):
        print(f"Periodo {periodo} correctamente iniciado")

    def cerrar_periodo(self,cerrar):
        print(f"Desea cerrar el periodo actual? {cerrar}")
        cerrar = cerrar.strip().lower()
        if cerrar == "si":
            print("Periodo cerrado")

    def consultar_periodo(self,periodo_conslt):
        print(f"Informacion del periodo {periodo_conslt}")
        print(f"Inicio: {self._fecha_inicio}")
        print(f"Finaliza: {self._fecha_final}")
        print(f"Estado actual: {self._estado}")

Periodo =  Periodo_Academico("15-septiembre", "7-Febrero","Inicidado")
Periodo.abrir_periodo("2025-2")
Periodo.cerrar_periodo("No")
Periodo.consultar_periodo("2025-2")