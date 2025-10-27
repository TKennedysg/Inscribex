class Universidad:
    def __init__(self, nombre, ubicacion, profesores, estudiantes, carrera, malla_curricular):
        self.nombre = nombre                      
        self.ubicacion = ubicacion                
        self._profesores = profesores             
        self._estudiantes = estudiantes           
        self.carrera = carrera                    
        self._malla_curricular = malla_curricular 

    def Asignacion_Cupos(self):
        return f"Se han asignado cupos en la universidad '{self.nombre}' para la carrera {self.carrera}."

    def publicar_oferta(self):
        print(f"La universidad {self.nombre} ha publicado una nueva oferta academica.")

    def recibir_postulaciones(self):
        print(f"La universidad {self.nombre} esta recibiendo postulaciones de aspirantes.")

    def mostrar_malla(self):
        print(f"Malla curricular de {self.carrera}:")
        for materia in self._malla_curricular:
            print("-", materia)

uni = Universidad(
    nombre="Universidad Laica Eloy Alfaro de Manabí",
    ubicacion="Manta",
    profesores=["Prof. Jarol", "Prof. Ener Valencia"],
    estudiantes=["Pepito", "Pinocho"],
    carrera="Ingeniería de Software",
    malla_curricular=["Álgebra Lineal", "Programación Orientada a Objetos", "Modelado Orientado a Objetos"]
)
print(uni.Asignacion_Cupos())
uni.publicar_oferta()
uni.recibir_postulaciones()
uni.mostrar_malla()

# ------------------------------------------------------------------------------------------------------------------

class Sede:
    def __init__(self, nombre, direccion, ciudad):
        self.nombre = nombre          
        self._direccion = direccion   
        self.ciudad = ciudad          
        self.__activa = True         

    def asignar(self):
        print(f"Asignando recursos y personal a la sede {self.nombre}.")
    def registrar(self):
        print(f"Registrando la sede {self.nombre} con dirección {self._direccion} en el sistema.")
    def obtenerDatos(self):
        estado = "Activa" if self.__activa else "Inactiva"
        return f"Sede: {self.nombre}, Dirección: {self._direccion}, Ciudad: {self.ciudad}, Estado: {estado}"

sede1 = Sede(nombre="Sede Central", direccion="Av. Universidad Laica Eloy Alfaro", ciudad="Manta")
sede1.asignar()
sede1.registrar()
print(sede1.obtenerDatos())

# ------------------------------------------------------------------------------------------------------------------

class Jornada():
    def __init__(self,hora,modalidad=""):
        self.hora = hora
        self.modalidad = modalidad

    def asignar(self):
        print("Se ha asignado la jornada")
   
    def modificar(self):
        print("Jornada se ha modificado")

    def mostrar(self):
        print("-----Modalidades-----")
        print("Matutina")
        print("Vespertina")
        print("Nocturna")
   
    def consultar(self):
        print(f"Modalidad: {self.modalidad}")

        if self.hora >=7 and self.hora <=11:
            print("jornada matutina")
        elif self.hora >=12 and self.hora <=17:
            print("Jornada vespertina")
        elif self.hora >=18 and self.hora <=22:
            print("Jornada nocturna")
        else:
            print("la hora no perteneces a ninguna jornada")

J1 = Jornada(20,"virtual")
J1.consultar()

# ------------------------------------------------------------------------------------------------------------------

class Periodo_Academico:
    def __init__(self,fecha_inicio,fecha_final,estado):
        self.fecha_inicio=fecha_inicio
        self.fecha_final=fecha_final
        self.estado=estado

    def abrir_periodo(self,periodo):
        print(periodo)

    def cerrar_periodo(self):
        print("Periodo Terminado")

    def consultar_periodo(self):
        print("Periodo consultado")

Periodo =  Periodo_Academico("15-Septiemnbre", "7-Febrero","Inicidado")
Periodo.abrir_periodo(input("Ingrese el periodo a iniciar: "))
Periodo.cerrar_periodo()
Periodo.consultar_periodo()

# ------------------------------------------------------------------------------------------------------------------

class Carrera():
    def __init__(self,area,nombre,modalidad,malla):
        self.area = area
        self.nombre = nombre
        self.modalidad = modalidad
        self.malla = malla
    def mostrar(self):
        print(f"Area:{self.area}")
        print(f"Nombre:{self.nombre}")
        print(f"Modalidad:{self.modalidad}")
        print(f"Malla:{self.malla}")

class Oferta_academica():
    def __init__(self,facultad,carrera,jornada,cupos,modalidad):
        self.facultad = facultad
        self.carrera = carrera
        self.jornada = jornada
        self.cupos = cupos
        self.modalidad = modalidad

    def visualizar(self):
        print("-----OFERTA ACADEMICA-----")
        print(f"Facultad:{self.facultad}")
        self.carrera.mostrar()
        print(f"Jornada:{self.jornada}")
        print(f"Modalidades: {self.modalidad}")
        
    def publicar(self):
        print("Se ha publicado la oferta academica")

C1 = Carrera("Tecnologia","Tecnologia de la informacion","Presencial","2025")
oferta1 = Oferta_academica("Ciencias de la vida y la Tecnologia",C1,"Matutina",100,"Presencial")
oferta1.visualizar()
oferta1.publicar()

# ------------------------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------------------------

class Autenticacion():
    def __init__(self,correo,contraseña):
        self.correo = correo
        self.contraseña = contraseña
            
    def iniciar_sesion(self,correo_ingesado,contraseña_ingresada):
        if correo_ingesado == self.correo and contraseña_ingresada == self.contraseña: 
            print("Ha iniciado sesión")
        else:
            print("correo o contraseña incorrectos")
    

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


Autenticacion1 = Autenticacion("tyrone27@gmail.com","123321")
Inscripcion1 = Inscripcion("tyrone","26/10/2025","123",Autenticacion1,)

Inscripcion1.ingresar_datos()
Inscripcion1.registrarse()


# ------------------------------------------------------------------------------------------------------------------

class Registro:
    def __init__(self, idRegistro, correo, estado):
        print(f"Se ha creado el registro {idRegistro} con correo {correo} y estado {estado}")
        self.idRegistro = idRegistro
        self.correo = correo
        self.estado = estado

    def registrar(self):
        print(f"El registro {self.idRegistro} ha sido guardado.")

    def actualizarEstado(self, nuevo_estado):
        print(f"El registro {self.idRegistro} cambia de {self.estado} a {nuevo_estado}")
        self.estado = nuevo_estado

    def obtenerDatos(self):
        print(f"Datos = ID: {self.idRegistro}, Correo: {self.correo}, Estado: {self.estado}")

simulacion1 = Registro("411", "karpite@gmail.com", "En proceso")
simulacion1.registrar()
simulacion1.actualizarEstado("Terminado")
simulacion1.obtenerDatos()

# ------------------------------------------------------------------------------------------------------------------

class ValidacionRegistro:
    def __init__(self, fecha_validacion, resultado, observacion):
        self.fecha_validacion = fecha_validacion
        self.resultado = resultado
        self.observacion = observacion

    def verificarRegistro(self, estado_documentos):
        if estado_documentos:
            self.resultado = "Validado"
            self.observacion = "Documentos validos."
        else:
            self.resultado = "Rechazado"
            self.observacion = "Faltan documentos o estan incorrectos."
        return self.resultado

    def aprobar(self):
        print(f"Registro aprobado, su Observacion: {self.observacion}")

    def generarResultado(self):
        return f"Fecha: {self.fecha_validacion}, Resultado: {self.resultado}, Observacion: {self.observacion}"

    def obtenerEstado(self):
        return self.resultado
    
validacion = ValidacionRegistro(fecha_validacion="26/10/2025", resultado="", observacion="")
print(validacion.verificarRegistro(True))
validacion.aprobar()
print(validacion.generarResultado())
print("Estado actual:", validacion.obtenerEstado())

# ------------------------------------------------------------------------------------------------------------------

class Examen:
    def __init__(self, area, preguntas, horario, tipo, calificacion):
        self.area = area
        self.preguntas = preguntas
        self.horario = horario
        self.tipo = tipo
        self.calificacion = calificacion

    def realizar_examen(self):
        print(f"Realizando un examen de {self.area} con {self.preguntas} preguntas.")
    
    def generar_reporte(self):
        print(f"El examen de {self.area} fue de tipo {self.tipo} y obtuvo una calificación de {self.calificacion}.")
    
    def calificar_examen(self, nueva_calificacion):
        self.calificacion = nueva_calificacion
        print (f"La calificación del examen de {self.area} ha sido actualizada a {self.calificacion}.")

ex = Examen("Matemáticas, Fisica", 60, "10:00 AM - 25-10-2025 ", "Teórico-Practico", 650)
ex.realizar_examen()
ex.generar_reporte()
ex.calificar_examen(720)
ex.generar_reporte()

# ------------------------------------------------------------------------------------------------------------------

class PlanificacionExamen:
    def __init__(self, fecha, aula, horarios_disponibles, capacidad, planificacion, cantidad, monitoreo):
        self.__fecha = fecha                        
        self.__aula = aula                          
        self._horarios_disponibles = horarios_disponibles  
        self.__capacidad = capacidad                
        self.planificacion = planificacion         
        self._cantidad = cantidad                   
        self.__monitoreo = monitoreo                
        self.__participantes = []                    

    def Asignar(self, aspirante):
        if len(self.__participantes) < self.__capacidad:
            self.__participantes.append(aspirante)
            return f"Aspirante {aspirante} ha sido asignado al examen del {self.__fecha} en el aula {self.__aula}."
        else:
            return f"No se puede asignar, el aula {self.__aula} alcanzó su capacidad máxima ({self.__capacidad})."
    
    def Organizar(self):
        return f"Examen organizado en {self.__aula} con capacidad de {self.__capacidad} alumnos bajo modalidad '{self.planificacion}'."

    def Generar_Cronograma(self):
        return f"Cronograma generado. Aula: {self.__aula}, Planificación: {self.planificacion}, Monitoreo: {self.__monitoreo}."
    
plan_examen = PlanificacionExamen(
    fecha="10/11/2025",
    aula="A101",
    horarios_disponibles=["08:00-10:00", "10:30-12:30"],
    capacidad=2,
    planificacion="Presencial",
    cantidad=30,
    monitoreo="Supervisor 3"
)
print(plan_examen.Asignar("Pepito Perez"))
print(plan_examen.Asignar("Kennedy Lopez"))
print(plan_examen.Asignar("Chito Vera"))
print(plan_examen.Organizar())
print(plan_examen.Generar_Cronograma())

# ------------------------------------------------------------------------------------------------------------------

class examenResultado:
    def __init__(self, calificacion, estado, fecha):
        self.calificacion = calificacion
        self.estado = estado
        self.fecha = fecha
    
    def revisarResultado(self):
        if self.calificacion >= 600:
            self.estado = "Aprobado"
        else:
            self.estado = "Reprobado"
        return self.estado
    
    def validarResultado(self):
        if self.estado == "Aprobado":
            print("El examen ha sido aprobado.")
        else:
            print("El examen no ha sido aprobado.")

    def obtenerreporte(self):
        reporte = f"Fecha: {self.fecha}, Calificación: {self.calificacion}, Estado: {self.estado}"
        return reporte
resex = examenResultado(600, "Pendiente", "2025-10-15")
resex.revisarResultado()
resex.obtenerreporte()
resex.validarResultado()

# ------------------------------------------------------------------------------------------------------------------

class Nota_postulacion():
    def __init__(self,nota_examen,puntaje_extra):
        self.nota_examen = nota_examen
        self.puntaje_extra = puntaje_extra
        self.puntaje_final = 0
    
    def calcular_nota(self):
        self.puntaje_final = (self.nota_examen/2)+(self.puntaje_extra/2)
        print("Se esta calculado la nota...")
        return self.puntaje_final
    def Obtener_nota(self):
        print(f"La nota obtenida es: {self.puntaje_final}")

N1 = Nota_postulacion(500,900)
N1.calcular_nota()
N1.Obtener_nota()

# ------------------------------------------------------------------------------------------------------------------

class Postulacion:
    def __init__(self,fecha_postulacion,calificacion_obtenida,estado,prioridad):
        print(f"Se ha postulado en la fecha {fecha_postulacion} con una calificacion de {calificacion_obtenida}, estado {estado}, con prioridad {prioridad}")
        self.fecha_postulacion=fecha_postulacion
        self.estado=estado
        self.calificacion_obtenida=calificacion_obtenida
        self.prioridad=prioridad

    def escoger_carrera(self,carrera):
        print("Ingrese la caerra a la que desea postular: ",carrera)
   
    def confirmar_seleccion(self,):
        print("Esta seguro de que desea postular a esa carrea? ")
    
    def cancelar_seleccion(self,seleccion):
        if seleccion == "No":
            print("Selección cancelada")
        else:
            print("Selección confirmada")
    
simulacion1 =  Postulacion("5-Octubre", "500","En proceso","Ninguna")
simulacion1.escoger_carrera("Arquitectura")
simulacion1.confirmar_seleccion()
simulacion1.cancelar_seleccion(input())

# ------------------------------------------------------------------------------------------------------------------

class Historial:
    def __init__ (self, aspirante, fecha_actualizada, estado):
        self.aspirante = aspirante
        self.fecha_actualizada = fecha_actualizada
        self.estado = estado

    def registrar_historial(self):
        print(f"Historial registrado para {self.aspirante} el {self.fecha_actualizada} con estado: {self.estado}")
    
    def consultar_historial(self):
        print (f"Aspirante: {self.aspirante}, Fecha Actualizada: {self.fecha_actualizada}, Estado: {self.estado}")
    
    def limpiar_historial(self):
        self.aspirante = ""
        self.fecha_actualizada = ""
        self.estado = ""
        print("Historial limpiado.")
hist = Historial("Ana Gomez", "2025-10-25", "Activo")
hist.registrar_historial()
hist.consultar_historial()  
hist.limpiar_historial()