class aspirante:
    def __init__(self,nombre,cedula,correo,telefono,direccion):
        self.nombre=nombre
        self.__cedula=cedula
        self._correo=correo
        self._telefono=telefono
        self._direccion=direccion
    def Registrarse(self):
        print("Aspirante Registrado")
        print("Nombre: ",self.nombre)
        print("Cedula: ",self.__cedula)
        print("Correo: ",self._correo)
        print("Telefono: ",self._telefono)
        print("Direccion: ",self._direccion)
    def postularse(self):
        print("Aspirante Postulado")
        print("Nombre: ",self.nombre)
        print("Cedula: ",self.__cedula)
    def consultarEstado(self):
        print("Consultando estado de Aspirante")
        print("Nombre: ",self.nombre)
        print("Cedula: ",self.__cedula)

asp = aspirante("Juan Perez","1309768932","juan.perez@gmail.com","0987654321","Av. Siempre Falsa 33")
asp.Registrarse()
asp.postularse()
asp.consultarEstado()