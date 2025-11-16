class Autenticacion():
    def __init__(self):
        self.__correo = None
        self.__contraseña = None

    def registrarse(self):
        print("\n===== REGISTRO DE USUARIO =====")

        correo = input("Ingrese su correo: ")
        contraseña = input("Ingrese su contraseña: ")
        self.__correo = correo      
        self.__contraseña = contraseña
        
        print("Se ha registrado con éxito")
        
    def iniciar_sesion(self):   
        print("\n===== REGISTRO DE USUARIO =====")
        
        correo_ingresado = input("Ingrese su correo: ")
        contraseña_ingresada = input("Ingrese su contraseña: ")

        if correo_ingresado == self.__correo and contraseña_ingresada == self.__contraseña: 
            print("Ha iniciado sesión")
        else:
            print("correo o contraseña incorrectos")


# MENÚ DE AUTENTICACIÓN
def menu_autenticacion():
    sistema = Autenticacion()

    while True:
        print("===== MÓDULO DE AUTENTICACIÓN =====")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.registrarse()
        elif opcion == "2":
            sistema.iniciar_sesion()
        elif opcion == "3":
            print("Saliendo del módulo...")
            break
        else:
            print("Opción no válida\n")


# EJECUCIÓN DEL MÓDULO
if __name__ == "__main__":
    menu_autenticacion()