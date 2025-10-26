class Postulacion:
    def __init__(self,fecha_postulacion,estado,calificacion_obtenida,prioridad):
        self.fecha_postulacion=fecha_postulacion
        self.estado=estado
        self.calificacion_obtenida=calificacion_obtenida
        self.prioridad=prioridad

    def escoger_carrera(self,carrera):
        print(f"Ingrese la caerra a la que desea postular: ",carrera)
   
    def confirmar_seleccion(self,seleccion):
        print("Esta seguro? ",seleccion)
    
    def cancelar_seleccion(self):
        print("Seleccion cancelada")
    
simulacion1 =  Postulacion("5-Octubre", "En proceso","500","Ninguna")
simulacion1.escoger_carrera("Arquitectura")
simulacion1.confirmar_seleccion("Si")
simulacion1.cancelar_seleccion()