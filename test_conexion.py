from database import ConexionDB

def probar():
    print("Intentando conectar...")
    db = ConexionDB() # Usa los datos que pusiste en database.py
    db.conectar()
    
    if db.connection:
        print("✅ ¡ÉXITO! Conexión lograda con PostgreSQL.")
        # Consultamos la versión para presumir
        version = db.ejecutar_consulta("SELECT version();")
        print(f"Versión de la Base de Datos: {version[0][0]}")
        db.cerrar()
    else:
        print("❌ FALLÓ. Revisa tu contraseña en database.py")

if __name__ == "__main__":
    probar()