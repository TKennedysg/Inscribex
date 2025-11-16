# usuarios.py
from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, cedula, correo, contrasena):
        self.nombre = nombre
        self.cedula = cedula 
        self.correo = correo
        self.contrasena = contrasena
    
    @abstractmethod
    def Registrarse(self):
        pass


class Aspirante(Usuario):
    def __init__(self, nombre, cedula, correo, contrasena, telefono, direccion):
        super().__init__(nombre, cedula, correo, contrasena)
        self.telefono = telefono
        self.direccion = direccion

    def Registrarse(self):
        print("Aspirante Registrado")
        print("Nombre: ", self.nombre)
        print("Cedula: ", self.cedula)
        print("Correo: ", self.correo)
        print("Telefono: ", self.telefono)
        print("Direccion: ", self.direccion)

    def postularse(self):
        print(f"{self.nombre} se ha postulado correctamente.")

    def consultarEstado(self):
        print(f"El estado del aspirante {self.nombre} está en revisión.")


class Administrador(Usuario):
    def __init__(self, nombre, cedula, correo, contrasena):
        super().__init__(nombre, cedula, correo, contrasena)

    def Registrarse(self):
        print("Administrador Registrado")
        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Correo: {self.correo}")
