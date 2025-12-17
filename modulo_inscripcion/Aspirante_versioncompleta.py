from abc import ABC, abstractmethod
from datetime import datetime

# --- CLASE BASE (que faltaba) ---
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

# --- CLASE ASPIRANTE MODIFICADA ---
class Aspirante(Usuario):
    # Constructor simplificado para uso interno del Builder
    def __init__(self, nombre, cedula, correo):
        super().__init__(nombre, cedula, correo)
        self.telefono = None
        self.direccion = None
        self.__estado = "pre-inscrito"
        self.__documentos = {}

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, nuevo_estado):
        # Validación simple
        estados_validos = ["pre-inscrito", "inscrito", "validado", "admitido", "rechazado", "completado"]
        if nuevo_estado in estados_validos:
            self.__estado = nuevo_estado

    def registrarse(self):
        print("🎓 REGISTRO DE ASPIRANTE")
        print("=" * 40)
        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Correo: {self.correo}")
        # Usamos getattr por si son None
        print(f"Teléfono: {getattr(self, 'telefono', 'No registrado')}") 
        print(f"Dirección: {getattr(self, 'direccion', 'No registrada')}")
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

# --- PATRÓN BUILDER ---
class AspiranteBuilder:
    def __init__(self):
        self.nombre = None
        self.cedula = None
        self.correo = None
        self.telefono = None
        self.direccion = None

    def con_datos_personales(self, nombre, cedula, correo):
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo
        return self # Retornamos self para encadenar

    def con_contacto(self, telefono, direccion):
        self.telefono = telefono
        self.direccion = direccion
        return self

    def build(self):
        # Validación básica antes de construir
        if not all([self.nombre, self.cedula, self.correo]):
            raise Exception("Faltan datos obligatorios para crear el Aspirante")
        
        # Construimos el objeto real
        aspirante = Aspirante(self.nombre, self.cedula, self.correo)
        aspirante.telefono = self.telefono
        aspirante.direccion = self.direccion
        return aspirante