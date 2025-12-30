from aspirante import Aspirante
from admin import Administrador 
from autenticacion import Autenticacion
from observer.notificaciones import Notificacion    

# Crear sistema de autenticación
auth = Autenticacion()

# Crear usuarios
asp1 = Aspirante("Juan Perez", "1309768932", "juan@gmail.com", "1234","0987654321", "Av. Los Eucaliptos 123",None)
asp2 = Aspirante("Maria Lopez", "1309768933", "maria@gmail.com","123","0987654321","La epoca",None)
admin1 = Administrador("Santiago", "1234567899", "santy@gmail.com", "admin123")

# Registrar usuarios en el sistema
auth.registrar_usuario(asp1)
auth.registrar_usuario(asp2)    
auth.registrar_usuario(admin1)

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
