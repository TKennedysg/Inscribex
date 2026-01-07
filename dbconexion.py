import os
import psycopg2
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Prueba de conexión
if __name__ == "__main__":
    connection = get_db_connection()
    if connection:
        print("¡Conexión exitosa usando variables de entorno!")
        connection.close()