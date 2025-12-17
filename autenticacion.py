class Autenticacion():
    def __init__(self,correo,contraseña):
        self.__correo = correo
        self.__contraseña = contraseña
        
    def iniciar_sesion(self,correo_ingresado,contraseña_ingresada):   
        if correo_ingresado == self.__correo and contraseña_ingresada == self.__contraseña: 
            print("Ha iniciado sesión")
        else:
            print("correo o contraseña incorrectos")



