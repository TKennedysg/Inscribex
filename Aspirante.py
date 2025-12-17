from abc import ABC, abstractmethod
from datetime import datetime

class Usuario(ABC):
    def __init__(self, nombre, cedula, correo):
        self.__nombre = nombre
        self.__cedula = cedula 
        self.__correo = correo
        self.__fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def cedula(self):
        return self.__cedula
    
    @property
    def correo(self):
        return self.__correo
    
    @property
    def fecha_registro(self):
        return self.__fecha_registro

    @abstractmethod
    def registrarse(self):
        pass

class Aspirante(Usuario):
    def __init__(self, nombre, cedula, correo, telefono, direccion, estado="pre-inscrito"):
        super().__init__(nombre, cedula, correo)
        self.__telefono = telefono
        self.__direccion = direccion
        self.__estado = estado
        self.__documentos = {}

    @property
    def telefono(self):
        return self.__telefono
    
    @property
    def direccion(self):
        return self.__direccion
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, nuevo_estado):
        estados_validos = ["pre-inscrito", "inscrito", "validado", "admitido", "rechazado"]
        if nuevo_estado in estados_validos:
            self.__estado = nuevo_estado
        else:
            print(f"Estado no válido: {nuevo_estado}")

    def registrarse(self):
        print("🎓 REGISTRO DE ASPIRANTE")
        print("=" * 40)
        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Correo: {self.correo}")
        print(f"Teléfono: {self.__telefono}")
        print(f"Dirección: {self.__direccion}")
        print(f"Fecha: {self.fecha_registro}")
        print("✅ Aspirante registrado exitosamente")
        return True

    def consultar_estado(self):
        estado_icon = {
            "pre-inscrito": "⏳",
            "inscrito": "📝", 
            "validado": "✅",
            "admitido": "🎓",
            "rechazado": "❌"
        }
        icon = estado_icon.get(self.__estado, "🔍")
        return f"{icon} {self.nombre} - Estado: {self.__estado} - Cédula: {self.cedula}"

    def agregar_documento(self, tipo_documento, archivo):
        documentos_permitidos = ["documento_identidad", "certificado_estudios", "foto", "hoja_vida"]
        if tipo_documento in documentos_permitidos:
            self.__documentos[tipo_documento] = archivo
            print(f"📄 Documento '{tipo_documento}' agregado")
            return True
        else:
            print(f"Tipo de documento no permitido: {tipo_documento}")
            return False

    def obtener_documentos(self):
        return self.__documentos

# Ejemplo de prueba
if __name__ == "__main__":
    asp = Aspirante("Juan", "123", "juan@email.com", "0991112222", "Av. Test 123")
    asp.registrarse()
    asp.agregar_documento("documento_identidad", "cedula.pdf")
    print(asp.consultar_estado())