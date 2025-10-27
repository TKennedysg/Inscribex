class Autenticacion():
    def __init__(self,correo,contraseña):
        self.correo = correo
        self.contraseña = contraseña
            
    def iniciar_sesion(self,correo_ingesado,contraseña_ingresada):
        if correo_ingesado == self.correo and contraseña_ingresada == self.contraseña: 
            print("Ha iniciado sesión")
        else:
            print("correo o contraseña incorrectos")

Autenticacion1 = Autenticacion("tyrone27@gmail.com","123321")