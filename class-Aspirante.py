class aspirante:
    def __init__(self,nombre,cedula,correo,telefono,direccion):
        self.nombre=nombre
        self.cedula=cedula
        self.correo=correo
        self.telefono=telefono
        self.direccion=direccion
        pass
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