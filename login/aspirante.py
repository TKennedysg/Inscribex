from usuario import Usuario
from observer.subject import Subject    

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