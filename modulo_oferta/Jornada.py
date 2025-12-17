class Jornada:
    def __init__(self, tipo):
        self.tipo = tipo  # Matutina, Vespertina, Nocturna

    def mostrar(self):
        print(f"Jornada: {self.tipo}")