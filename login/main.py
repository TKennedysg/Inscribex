from aspirante import Aspirante
from admin import Administrador 
from autenticacion import Autenticacion
from observer.notificaciones import Notificacion    

# Crear sistema de autenticación
auth = Autenticacion()

# Crear usuarios
#datos aspirante

print("=== REGISTRO DE ASPIRANTE ===")

nombre = input("Ingrese nombre: ")
cedula = input("Ingrese cédula: ")
correo = input("Ingrese correo: ")
contraseña = input("Ingrese contraseña: ")
telefono = input("Ingrese teléfono: ")
direccion = input("Ingrese dirección: ")
estado = "Registrado"

aspirante = Aspirante(nombre, cedula, correo, contraseña , telefono, direccion, estado)

#datos personales
nacionalidad = input("Ingrese nacionalidad: ")
fecha_nacimiento = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")
estado_civil = input("Ingrese estado civil: ")
sexo = input("Ingrese sexo: ")
autoidentificacion = input("Ingrese autoidentificación: ")
discapacidad = input("¿Tiene alguna discapacidad? (Sí/No): ")    
pais = input("Ingrese país: ")
provincia = input("Ingrese provincia: ")
ciudad = input("Ingrese ciudad: ")

#datos vivienda 
barrio = input("Ingrese barrio: ")
calle_principal = input("Ingrese calle principal: ")
calle_secundaria = input("Ingrese calle secundaria: ")
numero_domicilio = input("Ingrese número de domicilio: ")
tipo_vivienda = input("Ingrese tipo de vivienda: ")
agua_potable = input("¿Tiene agua potable? (Sí/No): ")
energia_electrica = input("¿Tiene energía eléctrica? (Sí/No): ")
alcantarillado = input("¿Tiene alcantarillado? (Sí/No): ")
recoleccion_basura = input("¿Tiene recolección de basura? (Sí/No): ")
internet = input("¿Tiene internet? (Sí/No): ")
dispositivos_tecnologicos = input("¿Tiene dispositivos tecnológicos? (Sí/No): ")
    
#datos academicos
titulo_homologado = input("Ingrese título homologado: ")
unidad_educatica = input("Ingrese unidad educática: ")
tipo_unidad_educativa = input("Ingrese tipo de unidad educativa: ")
calificacion = input("Ingrese calificación: ")
cuadro_honor = input("¿Tiene cuadro de honor? (Sí/No): ")
titulo_tercer_nivel = input("Ingrese título de tercer nivel: ")
titulo_cuarto_nivel = input("Ingrese título de cuarto nivel: ")
fecha_registro_nacional = input("Ingrese fecha de registro nacional (YYYY-MM-DD): ")

# Registrar usuarios en el sistema
auth.registrar_usuario(aspirante)

# --------- LOGIN ---------
print("\n--- INICIO DE SESIÓN ---")
correo = input("Correo: ")
contrasena = input("Contraseña: ")

usuario_logueado = auth.login(correo, contrasena)

# Si inicia sesión, usar funciones según el tipo de usuario
if usuario_logueado:
    if isinstance(usuario_logueado, Aspirante):
        print("\n--- Aspirante ---")
        usuario_logueado.consultarEstado()
        notif = Notificacion()

        # Se registra el observer
        usuario_logueado.agregar_observer(notif)

        usuario_logueado.Registrarse()     # la notificación
        usuario_logueado.consultarEstado()
        usuario_logueado.postularse()      # la notificación
        usuario_logueado.consultarEstado()


    elif isinstance(usuario_logueado, Administrador):
        print("\n--- Menú Administrador ---")
        usuario_logueado.Registrarse()
