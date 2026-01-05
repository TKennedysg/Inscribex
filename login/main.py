from aspirante import Aspirante
from admin import Administrador 
from autenticacion import Autenticacion
from observer.notificaciones import Notificacion    

# Crear sistema de autenticación
auth = Autenticacion()

# Crear usuarios

print("=== REGISTRO DE ASPIRANTE ===")

nombre = input("Ingrese nombre: ")
cedula = input("Ingrese cédula: ")
correo = input("Ingrese correo: ")
contraseña = input("Ingrese contraseña: ")
telefono = input("Ingrese teléfono: ")
direccion = input("Ingrese dirección: ")
estado = "Registrado"

aspirante = Aspirante(nombre, cedula, correo, contraseña , telefono, direccion, estado)

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
