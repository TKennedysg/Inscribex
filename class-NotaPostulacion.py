class Nota_postulacion():
    def __init__(self,nota_examen,puntaje_extra):
        self.__nota_examen = nota_examen
        self.__puntaje_extra = puntaje_extra
        self.__puntaje_final = 0
    
    def calcular_nota(self):
        self.__puntaje_final = (self.__nota_examen/2)+(self.__puntaje_extra/2)
        print("Se esta calculado la nota...")
        return self.__puntaje_final
    def Obtener_nota(self):
        print(f"La nota obtenida es: {self.__puntaje_final}")

N1 = Nota_postulacion(600,850)
N1.calcular_nota()
N1.Obtener_nota()