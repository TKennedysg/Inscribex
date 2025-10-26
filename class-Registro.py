class Registro:
    def __init__(self, idRegistro, correo, estado):
        print(f"Se ha creado el registro {idRegistro} con correo {correo} y estado {estado}")
        self.idRegistro = idRegistro
        self.correo = correo
        self.estado = estado

    def registrar(self):
        print(f"El registro {self.idRegistro} ha sido guardado.")

    def actualizarEstado(self, nuevo_estado):
        print(f"El registro {self.idRegistro} cambia de {self.estado} a {nuevo_estado}")
        self.estado = nuevo_estado

    def obtenerDatos(self):
        print(f"Datos = ID: {self.idRegistro}, Correo: {self.correo}, Estado: {self.estado}")

simulacion1 = Registro("411", "karpite@gmail.com", "En proceso")
simulacion1.registrar()
simulacion1.actualizarEstado("Terminado")
simulacion1.obtenerDatos()