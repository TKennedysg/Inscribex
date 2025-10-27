class Carrera():
    def __init__(self,area,nombre,modalidad,malla):
        self.__area = area
        self.__nombre = nombre
        self._modalidad = modalidad
        self.__malla = malla
    def mostrar(self):
        print(f"Area:{self.__area}")
        print(f"Nombre:{self.__nombre}")
        print(f"Modalidad:{self._modalidad}")
        print(f"Malla:{self.__malla}")