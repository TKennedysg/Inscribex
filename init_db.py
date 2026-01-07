import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def crear_tabla():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            apellido VARCHAR(100) NOT NULL,
            cedula VARCHAR(20) UNIQUE NOT NULL,
            contrasena VARCHAR(255) NOT NULL,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
    )
    
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        cur = conn.cursor()
        
        # Ejecutar los comandos
        for command in commands:
            cur.execute(command)
        
        cur.close()
        conn.commit()
        print("✅ Tabla 'usuarios' creada o verificada exitosamente.")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"❌ Error: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    crear_tabla()