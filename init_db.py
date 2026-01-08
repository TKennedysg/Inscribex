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
            telefono VARCHAR(20) NOT NULL,
            direccion VARCHAR(255) NOT NULL,
            estado VARCHAR(20) DEFAULT 'Registrado',
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        # 2. DATOS DEMOGRÁFICOS (Vinculado a usuarios)
        """
        CREATE TABLE IF NOT EXISTS datos_demograficos (
            id SERIAL PRIMARY KEY,
            usuario_id INTEGER UNIQUE NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
            nacionalidad VARCHAR(50) NOT NULL,
            fecha_nacimiento DATE NOT NULL,
            estado_civil VARCHAR(20) NOT NULL,
            sexo VARCHAR(20) NOT NULL,
            autoidentificacion VARCHAR(50) NOT NULL,
            discapacidad VARCHAR(5) NOT NULL,
            pais VARCHAR(50) NOT NULL,
            provincia VARCHAR(50) NOT NULL,
            ciudad VARCHAR(50) NOT NULL
        )
        """,
        # 3. DOMICILIO
        """
        CREATE TABLE IF NOT EXISTS domicilio (
            id SERIAL PRIMARY KEY,
            usuario_id INTEGER UNIQUE NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
            barrio VARCHAR(100) NOT NULL,
            calle_principal VARCHAR(100) NOT NULL,
            calle_secundaria VARCHAR(100) NOT NULL,
            numero_domicilio VARCHAR(20) NOT NULL,
            tipo_vivienda VARCHAR(50) NOT NULL
        )
        
        """,
        # 4. SERVICIOS BÁSICOS
        """
        CREATE TABLE IF NOT EXISTS servicios_basicos (
            id SERIAL PRIMARY KEY,
            usuario_id INTEGER UNIQUE NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
            agua_potable VARCHAR(5) NOT NULL,
            energia_electrica VARCHAR(5) NOT NULL,
            alcantarillado VARCHAR(5) NOT NULL,
            recoleccion_basura VARCHAR(5) NOT NULL,
            internet VARCHAR(5) NOT NULL
        )
        """,
        # 5. DATOS ACADÉMICOS
        """
        CREATE TABLE IF NOT EXISTS datos_academicos (
            id SERIAL PRIMARY KEY,
            usuario_id INTEGER UNIQUE NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
            titulo_homologado VARCHAR(100) NOT NULL,
            unidad_educativa VARCHAR(150) NOT NULL,
            tipo_unidad_educativa VARCHAR(50) NOT NULL,
            calificacion DECIMAL(5, 2) NOT NULL,
            cuadro_honor VARCHAR(5) NOT NULL,
            titulo_tercer_nivel VARCHAR(150) NOT NULL,
            titulo_cuarto_nivel VARCHAR(150) NOT NULL,
            fecha_registro_nacional DATE NOT NULL
        )
        """,
        # 7. JORNADAS ACADEMICAS
        """
        CREATE TABLE IF NOT EXISTS jornadas_academicas (
            id SERIAL PRIMARY KEY,
            nombre_jornada VARCHAR(50) NOT NULL UNIQUE
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