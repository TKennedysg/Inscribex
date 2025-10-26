class Sede:
    def __init__(self, nombre, direccion, ciudad):
        print(f"Sede {nombre} creada exitosamente en la ciudad de {ciudad}.")
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad

    def asignar(self):
        print(f"Asignando recursos y personal a la sede {self.nombre}.")

    def registrar(self):
        print(f"Registrando la sede {self.nombre} con dirección {self.direccion} en el sistema.")

    def mostrar(self):
        print(f"Información de la sede: {self.nombre}, ubicada en {self.direccion}, {self.ciudad}.")
