class Autenticacion():
    def __init__(self,correo,contraseña):
        self.correo = correo
        self.contraseña = contraseña
            
    def iniciar_sesion(self,correo_ingesado,contraseña_ingresada):
        if correo_ingesado == self.correo and contraseña_ingresada == self.contraseña: 
            print("Ha iniciado sesión")
        else:
            print("correo o contraseña incorrectos")
    

class Inscripcion():
    def __init__(self,aspirante,fecha,id_incripcion,autenticacion,estado="pendiente"):
        self.aspirante = aspirante
        self.fecha = fecha
        self.id_incripcion = id_incripcion
        self.autenticacion = autenticacion
        self.estado = estado

    def ingresar_datos(self):
        print("Se han ingredado los datos correctamente")
    def registrarse(self):
        print("se ha registrado correctamente")




