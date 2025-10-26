class Postulacion:
    def __init__(self,fecha_postulacion,estado,calificacion_obtenida,prioridad):
        self.fecha_postulacion=fecha_postulacion
        self.estado=estado
        self.calificacion_obtenida=calificacion_obtenida
        self.prioridad=prioridad

    def escoger_carrera(self):
        print("Ingrese la caerra a la que desea postular: ")
    def confirmar_seleccion(self):
        print("Esta seguro")
    def cancelar_seleccion(self):
        print("Ingrese el periodo: ")
    
simulacion1 =  Postulacion("5-Octubre", "En proceso","500","Ninguna")
simulacion1.abrir_periodo()
simulacion1.cerrar_periodo("Terminado")
simulacion1.consultar_periodo()