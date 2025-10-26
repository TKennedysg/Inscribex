class Carrera():
    def __init__(self,area,nombre,modalidad,malla):
        self.area = area
        self.nombre = nombre
        self.modalidad = modalidad
        self.malla = malla
    def mostrar(self):
        print(f"Area:{self.area}")
        print(f"Nombre:{self.nombre}")
        print(f"Modalidad:{self.modalidad}")
        print(f"Malla:{self.malla}")

class Oferta_academica():
    def __init__(self,facultad,carrera,jornada,cupos,modalidad):
        self.facultad = facultad
        self.carrera = carrera
        self.jornada = jornada
        self.cupos = cupos
        self.modalidad = modalidad

    def visualizar(self):
        print("-----OFERTA ACADEMICA-----")
        print(f"Facultad:{self.facultad}")
        self.carrera.mostrar()
        print(f"Jornada:{self.jornada}")
        print(f"Modalidades: {self.modalidad}")
        
    def publicar(self):
        print("Se ha publicado la oferta academica")

C1 = Carrera("Tecnologia","Tecnologia de la informacion","Presencial","2025")
oferta1 = Oferta_academica("Ciencias de la vida y la Tecnologia",C1,"Matutina",100,"Presencial")
oferta1.visualizar()
oferta1.publicar()