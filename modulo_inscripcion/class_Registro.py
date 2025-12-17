from datetime import datetime

class Registro:
    def __init__(self, idRegistro, aspirante, estado="pendiente"):
        self._idRegistro = idRegistro
        self.__aspirante = aspirante
        self.__correo = aspirante.correo
        self._estado = estado
        self.__fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Se ha creado el registro {idRegistro} para {aspirante.nombre} - Estado: {estado}")

    # GETTERS y SETTERS para mejor control
    @property
    def idRegistro(self):
        return self._idRegistro
    
    @property
    def estado(self):
        return self._estado
    
    @property
    def correo(self):
        return self.__correo
    
    @property
    def aspirante(self):
        return self.__aspirante

    def registrar(self):
        """Guarda el registro en el sistema"""
        self._estado = "registrado"
        print(f"Registro {self._idRegistro} guardado exitosamente - Fecha: {self.__fecha_registro}")
        return True

    def actualizarEstado(self, nuevo_estado):
        """Actualiza el estado del registro con validación"""
        estados_validos = ["pendiente", "en proceso", "completado", "rechazado", "cancelado"]
        
        if nuevo_estado in estados_validos:
            estado_anterior = self._estado
            self._estado = nuevo_estado
            print(f"Registro {self._idRegistro}: {estado_anterior} → {nuevo_estado}")
            return True
        else:
            print(f"Estado no válido: {nuevo_estado}")
            return False

    def obtenerDatos(self):
        """Retorna los datos del registro de forma estructurada"""
        datos = {
            'id': self._idRegistro,
            'aspirante': self.__aspirante.nombre,
            'cedula': self.__aspirante.cedula,
            'correo': self.__correo,
            'estado': self._estado,
            'fecha_registro': self.__fecha_registro
        }
        return datos

    def mostrarDatos(self):
        """Muestra los datos en formato legible"""
        datos = self.obtenerDatos()
        print(f"\n--- DATOS DEL REGISTRO ---")
        print(f"ID: {datos['id']}")
        print(f"Aspirante: {datos['aspirante']}")
        print(f"Cédula: {datos['cedula']}")
        print(f"Correo: {datos['correo']}")
        print(f"Estado: {datos['estado']}")
        print(f"Fecha: {datos['fecha_registro']}")

# Ejemplo de prueba
if __name__ == "__main__":
    from Aspirante_versioncompleta import Aspirante
    
    aspirante = Aspirante("Ana Lopez", "1309768932", "ana.lopez@gmail.com", "0987654321", "Av. Los Eucaliptos 123")
    registro = Registro("105", aspirante, "en proceso")
    registro.registrar()
    registro.actualizarEstado("completado")
    registro.mostrarDatos()