class Postulacion:
    def __init__(self,fecha_postulacion,calificacion_obtenida,estado,prioridad):
        print(f"Se ha postulado en la fecha {fecha_postulacion}" 
              f"con una calificacion de {calificacion_obtenida}, estado {estado}, con prioridad: {prioridad}")
        self._fecha_postulacion=fecha_postulacion
        self._estado=estado
        self.__calificacion_obtenida=calificacion_obtenida
        self._prioridad=prioridad

    def escoger_carrera(self,carrera):
        print("Carrera a postular escogida: ",carrera)
   
    def confirmar_seleccion(self,):
        print("Esta seguro de que desea postular a esa carrea? ")
    
    def cancelar_seleccion(self,seleccion):
        seleccion = seleccion.strip().lower()
        if seleccion == "no":
            print("Selección cancelada")
        else:
            print("Selección confirmada")
    
simulacion1 =  Postulacion("5-Octubre", "500","En proceso","Ninguna")
simulacion1.escoger_carrera("Arquitectura")
simulacion1.confirmar_seleccion()
simulacion1.cancelar_seleccion(input())