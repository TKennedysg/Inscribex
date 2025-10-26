class Nota_postulacion():
    def __init__(self,nota_examen,puntaje_extra):
        self.nota_examen = nota_examen
        self.puntaje_extra = puntaje_extra
        self.puntaje_final = 0
    
    def calcular_nota(self):
        self.puntaje_final = (self.nota_examen/2)+(self.puntaje_extra/2)
        print("Se esta calculado la nota...")
        return self.puntaje_final
    def Obtener_nota(self):
        print(f"La nota obtenida es: {self.puntaje_final}")

N1 = Nota_postulacion(500,900)
N1.calcular_nota()
N1.Obtener_nota()