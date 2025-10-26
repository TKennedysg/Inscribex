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
        print("Se han ingresado los datos correctamente")
    def registrarse(self):
        print("se ha registrado correctamente")
        correo = input("Ingrese su correo: ")
        contraseña = input("Ingrese su contraseña: ")
        self.autenticacion.iniciar_sesion(correo, contraseña)

            


Autenticacion1 = Autenticacion("tyrone27@gmail.com",123321)
Inscripcion1 = Inscripcion("tyrone","26/10/2025","123",Autenticacion1,)

Inscripcion1.ingresar_datos()
Inscripcion1.registrarse()

