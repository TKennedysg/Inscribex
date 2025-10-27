from autenticacion import Autenticacion

class Inscripcion():
    def __init__(self,aspirante,fecha,id_incripcion,autenticacion,estado="pendiente"):
        self.__aspirante = aspirante
        self.__fecha = fecha
        self.__id_incripcion = id_incripcion
        self.__autenticacion = autenticacion
        self._estado = estado

    def ingresar_datos(self):
        print("Se han ingresado los datos correctamente")
    def registrarse(self):
        print("se ha registrado correctamente")
        correo = input("Ingrese su correo: ")
        contraseña = input("Ingrese su contraseña: ")
        self.__autenticacion.iniciar_sesion(correo, contraseña)

Autenticacion1 = Autenticacion("tyrone27@gmail.com","123321")
Inscripcion1 = Inscripcion("tyrone","26/10/2025","123",Autenticacion1,)
Inscripcion1.ingresar_datos()
Inscripcion1.registrarse()

