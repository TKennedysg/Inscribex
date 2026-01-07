import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def crear_tablas():
    commands = (
        # 1. TABLA PRINCIPAL: USUARIOS
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            apellido VARCHAR(100) NOT NULL,
            cedula VARCHAR(20) UNIQUE NOT NULL,
            contrasena VARCHAR(255) NOT NULL,
            telefono VARCHAR(20),
            direccion TEXT,
            estado VARCHAR(20) DEFAULT 'Registrado',
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        # 2. DATOS DEMOGRÁFICOS (Vinculado a usuarios)
        """
        CREATE TABLE IF NOT EXISTS datos_demograficos (
            id SERIAL PRIMARY KEY,
            usuario_id INTEGER UNIQUE REFERENCES usuarios(id) ON DELETE CASCADE,
            nacionalidad VARCHAR(50),
            fecha_nacimiento DATE,
            estado_civil VARCHAR(20),
            sexo VARCHAR(20),
            autoidentificacion VARCHAR(50),
            discapacidad VARCHAR(5),
            pais VARCHAR(50),
            provincia VARCHAR(50),
            ciudad VARCHAR(50)
        )
        """,
        # 3. DOMICILIO
        """
        CREATE TABLE IF NOT EXISTS domicilio (
            id SERIAL PRIMARY KEY,
            usuario_id INTEGER UNIQUE REFERENCES usuarios(id) ON DELETE CASCADE,
            barrio VARCHAR(100),
            calle_principal VARCHAR(100),
            calle_secundaria VARCHAR(100),
            numero_domicilio VARCHAR(20),
            tipo_vivienda VARCHAR(50)
        )
        """,
        # 4. SERVICIOS BÁSICOS
        """
        CREATE TABLE IF NOT EXISTS servicios_basicos (
            id SERIAL PRIMARY KEY,
            usuario_id INTEGER UNIQUE REFERENCES usuarios(id) ON DELETE CASCADE,
            agua_potable VARCHAR(5),
            energia_electrica VARCHAR(5),
            alcantarillado VARCHAR(5),
            recoleccion_basura VARCHAR(5),
            internet VARCHAR(5),
            dispositivos_tecnologicos VARCHAR(5)
        )
        """,
        # 5. DATOS ACADÉMICOS
        """
        CREATE TABLE IF NOT EXISTS datos_academicos (
            id SERIAL PRIMARY KEY,
            usuario_id INTEGER UNIQUE REFERENCES usuarios(id) ON DELETE CASCADE,
            titulo_homologado VARCHAR(100),
            unidad_educativa VARCHAR(150),
            tipo_unidad_educativa VARCHAR(50),
            calificacion DECIMAL(5, 2),
            cuadro_honor VARCHAR(5),
            titulo_tercer_nivel VARCHAR(150),
            titulo_cuarto_nivel VARCHAR(150),
            fecha_registro_nacional DATE
        )
        """
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

        # Ejecutar los comandos en orden
        for command in commands:
            cur.execute(command)

        cur.close()
        conn.commit()
        print("✅ Todas las tablas han sido creadas o verificadas exitosamente.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"❌ Error al crear tablas: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    crear_tablas()