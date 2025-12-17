from observer.observer import Observer

class Notificacion(Observer):

    def actualizar(self, mensaje):
        print(f"Notificación recibida: {mensaje}")