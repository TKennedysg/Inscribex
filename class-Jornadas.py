class Jornada():
    def __init__(self,hora,modalidad=""):
        self.hora = hora
        self.modalidad = modalidad

    def asignar(self):
        print("Se ha asignado la jornada")
   
    def modificar(self):
        print("Jornada se ha modificado")

    def mostrar(self):
        print("-----Modalidades-----")
        print("Matutina")
        print("Vespertina")
        print("Nocturna")
   
    def consultar(self):
        print(f"Modalidad: {self.modalidad}")

        if self.hora >=7 and self.hora <=11:
            print("jornada matutina")
        elif self.hora >=12 and self.hora <=17:
            print("Jornada vespertina")
        elif self.hora >=18 and self.hora <=22:
            print("Jornada nocturna")
        else:
            print("la hora no perteneces a ninguna jornada")



J1 = Jornada(20,"virtual")
J1.consultar()
