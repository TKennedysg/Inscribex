class Periodo_Academico:
    def __init__(self,fecha_inicio,fecha_final,estado):
        self.fecha_inicio=fecha_inicio
        self.fecha_final=fecha_final
        self.estado=estado

    def abrir_periodo(self,periodo):
        print(periodo)

    def cerrar_periodo(self):
        print("Periodo Terminado")

    def consultar_periodo(self):
        print(f"Periodo consultado")

Periodo =  Periodo_Academico("15-Septiemnbre", "7-Febrero","Inicidado")
Periodo.abrir_periodo(input("Ingrese el periodo a iniciar: "))
Periodo.cerrar_periodo()
Periodo.consultar_periodo()