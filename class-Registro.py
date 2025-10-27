class Registro:
    def __init__(self, idRegistro, correo, estado):
        print(f"Se ha creado el registro {idRegistro} con el correo {correo} y en estado {estado}")
        self._idRegistro = idRegistro
        self.__correo = correo
        self._estado = estado

    def registrar(self):
        print(f"El registro {self._idRegistro} ha sido guardado.")

    def actualizarEstado(self, nuevo_estado):
        print(f"El registro {self._idRegistro} cambia de {self._estado} a {nuevo_estado}")
        self._estado = nuevo_estado

    def obtenerDatos(self):
        print(f"Datos = ID: {self._idRegistro}, Correo: {self.__correo}, Estado: {self._estado}")

simulacion1 = Registro("105", "karpite@gmail.com", "En proceso")
simulacion1.registrar()
simulacion1.actualizarEstado("Terminado")
simulacion1.obtenerDatos()