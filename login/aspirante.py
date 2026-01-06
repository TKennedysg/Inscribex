from usuario import Usuario
from observer.subject import Subject    

class Aspirante(Usuario, Subject):   # Ahora es Subject
    def __init__(self, nombre, cedula, correo,contraseña, telefono, direccion, estado):
        super().__init__(nombre, cedula, correo,contraseña)
        self.telefono = telefono
        self.direccion = direccion
        self._observers = []           # Lista de observadores
        self.estado = estado

    def datos_personales(self, nacionalidad, fecha_nacimiento, estado_civil, sexo , autoidentificacion, discapacidad, pais, provincia, ciudad ):
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.estado_civil = estado_civil
        self.sexo = sexo
        self.autoidentificacion = autoidentificacion
        self.discapacidad = discapacidad    
        self.pais = pais
        self.provincia = provincia
        self.ciudad = ciudad        
        

    def datos_vivienda(self, barrio, calle_principal, calle_secundaria, numero_domicilio, tipo_vivienda, agua_potable, energia_electrica, alcantarillado, recoleccion_basura, internet, dispositivos_tecnologicos):
        self.barrio = barrio
        self.calle_principal = calle_principal
        self.calle_secundaria = calle_secundaria
        self.numero_domicilio = numero_domicilio
        self.tipo_vivienda = tipo_vivienda
        self.agua_potable = agua_potable
        self.energia_electrica = energia_electrica
        self.alcantarillado = alcantarillado
        self.recoleccion_basura = recoleccion_basura
        self.internet = internet
        self.dispositivos_tecnologicos = dispositivos_tecnologicos
    
        
    def datos_academicos(self, titulo_homologado, unidad_educatica,tipo_unidad_educativa,calificacion, cuadro_honor, titulo_tercer_nivel, titulo_cuarto_nivel, fecha_registro_nacional, ):
        self.titulo_homologado = titulo_homologado
        self.unidad_educatica = unidad_educatica
        self.tipo_unidad_educativa = tipo_unidad_educativa
        self.calificacion = calificacion
        self.cuadro_honor = cuadro_honor
        self.titulo_tercer_nivel = titulo_tercer_nivel
        self.titulo_cuarto_nivel = titulo_cuarto_nivel
        self.fecha_registro_nacional = fecha_registro_nacional
        

    # MÉTODOS DEL SUBJECT
    def agregar_observer(self, observer): 
        self._observers.append(observer)

    def quitar_observer(self, observer):
        self._observers.remove(observer)

    def notificar(self, mensaje):
        for observer in self._observers:
            observer.actualizar(mensaje)

    #MÉTODOS DEL USUARIO 
   
    def Registrarse(self):
        self.estado = "Registrado"
        self.notificar(f"El aspirante {self.nombre} se ha registrado")
        print("Nombre:", self.nombre)
        print("Cedula:", self.cedula)
        print("Correo:", self.correo)


    #MÉTODOS ADICIONALES 

    def postularse(self):
        self.estado = "Postulado"
        self.notificar(f"El aspirante {self.nombre} se ha postulado")

    def consultarEstado(self):
        print(f"Estado actual: {self.estado}")