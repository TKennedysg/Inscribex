from carrera import Carrera 

class Oferta_academica():
    def __init__(self,facultad,carrera,jornada,cupos,modalidad):
        self.__facultad = facultad
        self.__carrera = carrera
        self.__jornada = jornada
        self._cupos = cupos
        self.__modalidad = modalidad

    def visualizar(self):
        print("-----OFERTA ACADEMICA-----")
        print(f"Facultad:{self.__facultad}")
        self.__carrera.mostrar()
        print(f"Jornada:{self.__jornada}")
        print(f"Modalidades: {self.__modalidad}")
        
    def publicar(self):
        print("Se ha publicado la oferta academica")

C1 = Carrera("Tecnologia","Tecnologia de la informacion","Presencial","2025")
oferta1 = Oferta_academica("Ciencias de la vida y la Tecnologia",C1,"Matutina",100,"Presencial")
oferta1.visualizar()
oferta1.publicar()