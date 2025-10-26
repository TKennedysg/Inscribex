class Sede:
    def __init__(self, nombre, direccion, ciudad):
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.activa = True

    def asignar(self):
        print(f"Asignando recursos y personal a la sede {self.nombre}.")

    def registrar(self):
        print(f"Registrando la sede {self.nombre} con dirección {self.direccion} en el sistema.")

    def obtenerDatos(self):
        return f"Sede: {self.nombre}, Direccion: {self.direccion}, Ciudad: {self.ciudad}, Estado: {'Activa' if self.activa else 'Inactiva'}"
