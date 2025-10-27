class aspirante:
    def __init__(self,nombre,cedula,correo,telefono,direccion):
        self.nombre=nombre
        self.cedula=cedula
        self.correo=correo
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

asp = aspirante("Juan Perez","1309768932","juan.perez@gmail.com","0987654321","Av. Siempre Falsa 33")
asp.Registrarse()
asp.postularse()
asp.consultarEstado()