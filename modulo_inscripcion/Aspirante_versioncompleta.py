from abc import ABC, abstractmethod
from datetime import datetime
from database import ConexionDB  # <--- IMPORTANTE: Importamos la conexión

# --- CLASE BASE ---
class Usuario(ABC):
    def __init__(self, nombre, cedula, correo):
        self.__nombre = nombre
        self.__cedula = cedula 
        self.__correo = correo
        self.__fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @property
    def nombre(self): return self.__nombre
    
    @property
    def cedula(self): return self.__cedula
    
    @property
    def correo(self): return self.__correo
    
    @property
    def fecha_registro(self): return self.__fecha_registro

    @abstractmethod
    def registrarse(self):
        pass

# --- CLASE ASPIRANTE CONECTADA A BD ---
class Aspirante(Usuario):
    def __init__(self, nombre, cedula, correo):
        super().__init__(nombre, cedula, correo)
        self.telefono = None
        self.direccion = None
        self.__estado = "pre-inscrito"
        self.__documentos = {}
        # Instanciamos la conexión
        self.db = ConexionDB() 

    # ... (Tus propiedades @estado y métodos de documentos se quedan igual) ...
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def agregar_documento(self, tipo, archivo):
        self.__documentos[tipo] = archivo

    def registrarse(self):
        """Guarda al aspirante en PostgreSQL"""
        print(f"📡 Registrando a {self.nombre} en la Base de Datos...")
        
        self.db.conectar()
        
        # SQL para insertar en la tabla 'usuarios'
        # Nota: Asignamos 'aspirante' como rol por defecto y password genérico '1234' por ahora
        sql = """
            INSERT INTO usuarios (cedula, nombre, correo, password, rol, telefono, direccion, estado)
            VALUES (%s, %s, %s, '1234', 'aspirante', %s, %s, %s)
        """
        
        # Valores a insertar
        datos = (
            self.cedula, 
            self.nombre, 
            self.correo, 
            self.telefono, 
            self.direccion, 
            self.__estado
        )
        
        try:
            self.db.cursor.execute(sql, datos)
            self.db.connection.commit() # Confirmar cambios
            print("✅ Aspirante guardado exitosamente en PostgreSQL.")
            return True
        except Exception as e:
            print(f"❌ Error al guardar en BD: {e}")
            self.db.connection.rollback()
            return False
        finally:
            self.db.cerrar()

    # ... (Resto de métodos como consultar_estado se mantienen igual) ...

# --- PATRÓN BUILDER (Sin cambios, solo funciona igual) ---
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
        return self 

    def con_contacto(self, telefono, direccion):
        self.telefono = telefono
        self.direccion = direccion
        return self

    def build(self):
        if not all([self.nombre, self.cedula, self.correo]):
            raise Exception("Faltan datos obligatorios")
        
        aspirante = Aspirante(self.nombre, self.cedula, self.correo)
        aspirante.telefono = self.telefono
        aspirante.direccion = self.direccion
        return aspirante

# --- PRUEBA RÁPIDA ---
if __name__ == "__main__":
    builder = AspiranteBuilder()
    
    # Crea un aspirante nuevo (Cambia la cédula si lo ejecutas varias veces)
    aspirante_prueba = (builder
        .con_datos_personales("Juan Bustamante", "1354565585", "juan.bd@email.com")
        .con_contacto("0992995912", "Calle SQL 123")
        .build()
    )
    
    aspirante_prueba.registrarse()