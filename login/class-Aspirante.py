from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, cedula, correo):
        self.nombre = nombre
        self.cedula = cedula 
        self.correo = correo
    
    @abstractmethod
    def Registrarse(self):
        pass

class Aspirante(Usuario):
    def __init__(self,nombre,cedula,correo,telefono,direccion):
        super().__init__(nombre, cedula, correo)
        self.telefono=telefono
        self.direccion=direccion

    def Registrarse(self):
        print("Aspirante Registrado")
        print("Nombre: ",self.nombre)
        print("Cedula: ",self.cedula)
        print("Correo: ",self.correo)
        print("Telefono: ",self.telefono)
        print("Direccion: ",self.direccion)

    def postularse(self):
        print("Aspirante Postulado")
        print("Nombre: ",self.nombre)
        print("Cedula: ",self.cedula)

    def consultarEstado(self):
        print("Consultando estado de Aspirante")
        print("Nombre: ",self.nombre)
        print("Cedula: ",self.cedula)

class Administrador(Usuario):
    def __init__(self, nombre, cedula, correo, ):
        super().__init__(nombre, cedula, correo)

    def Registrarse(self):
        print("Se ha registrado")
        print(f"Nombre: {self.nombre}") 
        print(f"Cédula: {self.cedula}")
        print(f"Correo: {self.correo}")

asp1 = Aspirante("Juan Perez","1309768932","juan.perez@gmail.com","0987654321","Av. Los Eucaliptos 123")
admin1 = Administrador("Santiago",1234567899,"santy123@gmail.com")

print("----ASPIRANTE----")
asp1.Registrarse()
asp1.postularse()
asp1.consultarEstado()

print("\n----ADMINISTRADOR----")
admin1.Registrarse()