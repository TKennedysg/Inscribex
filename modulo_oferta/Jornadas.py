# Jornadas.py
class Jornada:
    def __init__(self, tipo):
        self.tipo = tipo

    def mostrar(self):
        print(f"Jornada: {self.tipo}")