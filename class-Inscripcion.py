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

            
Inscripcion1 = Inscripcion("tyrone","26/10/2025","123",Autenticacion1,)

Inscripcion1.ingresar_datos()
Inscripcion1.registrarse()

