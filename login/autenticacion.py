# autenticacion.py
class Autenticacion:
    def __init__(self):
        self.usuarios_registrados = {}

    def registrar_usuario(self, usuario):
        self.usuarios_registrados[usuario.correo] = usuario

    def login(self, correo, contraseña):
        if correo in self.usuarios_registrados:
            usuario = self.usuarios_registrados[correo]
            if usuario.contraseña == contraseña:
                print("\n✔ LOGIN EXITOSO ✔")
                print(f"Bienvenido, {usuario.nombre}")
                return usuario
            else:
                print("Contraseña incorrecta")
        else:
            print("Usuario no encontrado")
        return None
