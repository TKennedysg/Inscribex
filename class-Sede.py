class Sede:
    def __init__(self, nombre, direccion, ciudad):
        self.nombre = nombre          
        self._direccion = direccion   
        self.ciudad = ciudad          
        self.__activa = True         

    def asignar(self):
        print(f"Asignando recursos y personal a la sede {self.nombre}.")
    def registrar(self):
        print(f"Registrando la sede {self.nombre} con dirección {self._direccion} en el sistema.")
    def obtenerDatos(self):
        estado = "Activa" if self.__activa else "Inactiva"
        return f"Sede: {self.nombre}, Dirección: {self._direccion}, Ciudad: {self.ciudad}, Estado: {estado}"

sede1 = Sede(nombre="Sede Central", direccion="Av. Universidad Laica Eloy Alfaro", ciudad="Manta")
sede1.asignar()
sede1.registrar()
print(sede1.obtenerDatos())