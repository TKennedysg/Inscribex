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

class Aspirante(Usuario, Subject):   # Ahora es Subject
    def __init__(self, nombre, cedula, correo,contraseña, telefono, direccion, estado):
        super().__init__(nombre, cedula, correo,contraseña)
        self.telefono = telefono
        self.direccion = direccion
        self._observers = []           # Lista de observadores
        self.estado = estado


    # MÉTODOS DEL SUBJECT
    def agregar_observer(self, observer): 
        self._observers.append(observer)

    def quitar_observer(self, observer):
        self._observers.remove(observer)

    def notificar(self, mensaje):
        for observer in self._observers:
            observer.actualizar(mensaje)

    #MÉTODOS DEL USUARIO 
   
    def Registrarse(self):
        self.estado = "Registrado"
        self.notificar(f"El aspirante {self.nombre} se ha registrado")
        print("Nombre:", self.nombre)
        print("Cedula:", self.cedula)
        print("Correo:", self.correo)


    #MÉTODOS ADICIONALES 

    def postularse(self):
        self.estado = "Postulado"
        self.notificar(f"El aspirante {self.nombre} se ha postulado")

    def consultarEstado(self):
        print(f"Estado actual: {self.estado}")


class Administrador(Usuario):
    def __init__(self, nombre, cedula, correo, contraseña):
        super().__init__(nombre, cedula, correo, contraseña)

    def Registrarse(self):
        print("Administrador Registrado")
        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Correo: {self.correo}")
