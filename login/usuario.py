# usuarios.py
from abc import ABC, abstractmethod
from observer.subject import Subject    

class Usuario(ABC):
    def __init__(self, nombre, cedula, correo,contraseña):
        self.nombre = nombre
        self.cedula = cedula 
        self.correo = correo
        self.contraseña = contraseña
    
    @abstractmethod
    def Registrarse(self):
        pass




