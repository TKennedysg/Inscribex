from usuario import Usuario 

class Administrador(Usuario):
    def __init__(self, nombre, cedula, correo, contraseña):
        super().__init__(nombre, cedula, correo, contraseña)

    def Registrarse(self):
        print("Administrador Registrado")
        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Correo: {self.correo}")
