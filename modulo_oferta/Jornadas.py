# Copia y pega esto en un nuevo archivo Jornada.py
class Jornada:
    """Clase que representa una jornada académica"""
    
    def __init__(self, tipo_jornada):
        """
        Inicializa una jornada
        
        Args:
            tipo_jornada (str): Tipo de jornada (Matutina, Vespertina, Nocturna)
        """
        self.tipo = tipo_jornada
    
    def mostrar(self):
        """Muestra información de la jornada"""
        print(f"Jornada: {self.tipo}")
    
    def __str__(self):
        return self.tipo
    
    def __repr__(self):
        return f"Jornada('{self.tipo}')"