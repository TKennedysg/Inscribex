class Carrera():
    def __init__(self,area,nombre,modalidad,malla):
        self.__area = area
        self.__nombre = nombre
        self._modalidad = modalidad
        self.__malla = malla
    def mostrar(self):
        print(f"Area:{self._area}")
        print(f"Nombre:{self._nombre}")
        print(f"Modalidad:{self._modalidad}")
        print(f"Malla:{self._malla}")