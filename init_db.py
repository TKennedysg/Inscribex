from dbconexion import get_db_connection


class Usuario:
    """
    Clase base del sistema SIPU (Sistema de Inscripción y Postulación Universitaria).
    Representa a cualquier usuario del sistema: ASPIRANTE o ADMIN.

    Esta clase NO contiene lógica de negocio.
    Su única responsabilidad es crear las tablas del sistema.
    """

    @staticmethod
    def crear_tablas():
        conn = get_db_connection()
        if conn is None:
            print("No se pudo conectar a la base de datos")
            return

        try:
            cursor = conn.cursor()

            # 1. TABLA PRINCIPAL: USUARIOS
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id SERIAL PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    apellido VARCHAR(100) NOT NULL,
                    cedula VARCHAR(20) UNIQUE NOT NULL,
                    contrasena VARCHAR(255) NOT NULL,
                    rol VARCHAR(20) DEFAULT 'ASPIRANTE',
                    estado VARCHAR(20) DEFAULT 'Registrado',
                    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # 2. DATOS DEMOGRÁFICOS (ETAPA: INSCRIPCIÓN)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS datos_demograficos (
                    id SERIAL PRIMARY KEY,
                    usuario_id INTEGER UNIQUE NOT NULL
                        REFERENCES usuarios(id) ON DELETE CASCADE,
                    nacionalidad VARCHAR(50) NOT NULL,
                    fecha_nacimiento DATE NOT NULL,
                    estado_civil VARCHAR(20) NOT NULL,
                    sexo VARCHAR(20) NOT NULL,
                    autoidentificacion VARCHAR(50) NOT NULL,
                    discapacidad VARCHAR(5) NOT NULL,
                    pais VARCHAR(50) NOT NULL,
                    provincia VARCHAR(50) NOT NULL,
                    ciudad VARCHAR(50) NOT NULL
                );
            """)

            # 3. DOMICILIO (ETAPA: INSCRIPCIÓN)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS domicilio (
                    id SERIAL PRIMARY KEY,
                    usuario_id INTEGER UNIQUE NOT NULL
                        REFERENCES usuarios(id) ON DELETE CASCADE,
                    barrio VARCHAR(100) NOT NULL,
                    calle_principal VARCHAR(100) NOT NULL,
                    calle_secundaria VARCHAR(100) NOT NULL,
                    numero_domicilio VARCHAR(20) NOT NULL,
                    tipo_vivienda VARCHAR(50) NOT NULL
                );
            """)

            # 4. SERVICIOS BÁSICOS (ETAPA: INSCRIPCIÓN)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS servicios_basicos (
                    id SERIAL PRIMARY KEY,
                    usuario_id INTEGER UNIQUE NOT NULL
                        REFERENCES usuarios(id) ON DELETE CASCADE,
                    agua_potable VARCHAR(5) NOT NULL,
                    energia_electrica VARCHAR(5) NOT NULL,
                    alcantarillado VARCHAR(5) NOT NULL,
                    recoleccion_basura VARCHAR(5) NOT NULL,
                    internet VARCHAR(5) NOT NULL
                );
            """)

            # 5. DATOS ACADÉMICOS (ETAPA: INSCRIPCIÓN)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS datos_academicos (
                    id SERIAL PRIMARY KEY,
                    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE CASCADE,
                    titulo_homologado VARCHAR(100) NOT NULL,
                    unidad_educativa VARCHAR(150) NOT NULL,
                    tipo_unidad_educativa VARCHAR(50) NOT NULL,
                    calificacion DECIMAL(5,2) NOT NULL,
                    cuadro_honor VARCHAR(5) NOT NULL,
                    titulo_tercer_nivel VARCHAR(150) NOT NULL,
                    titulo_cuarto_nivel VARCHAR(150) NOT NULL,
                    fecha_registro_nacional DATE NOT NULL
                );
            """)

            # 6. MODALIDAD
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS modalidad (
                    id SERIAL PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL UNIQUE
                );
            """)

            # 7. DURACIÓN DE CARRERAS
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS duracion_carreras (
                    id SERIAL PRIMARY KEY,
                    nombre_duracion VARCHAR(10) NOT NULL UNIQUE
                );
            """)

            # 8. DATOS CARRERAS (ETAPA: POSTULACIÓN)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS datos_carreras (
                    id SERIAL PRIMARY KEY,
                    usuario_id INTEGER NOT NULL
                        REFERENCES usuarios(id) ON DELETE CASCADE,
                    id_modalidad INTEGER NOT NULL
                        REFERENCES modalidad(id),
                    id_duracion_carrera INTEGER NOT NULL
                        REFERENCES duracion_carreras(id),
                    UNIQUE (usuario_id)
                );
            """)

            # 9. JORNADAS ACADÉMICAS
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS jornadas_academicas (
                    id SERIAL PRIMARY KEY,
                    nombre_jornada VARCHAR(50) NOT NULL UNIQUE
                );
            """)

            # 10. PERÍODOS ACADÉMICOS
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS periodos (
                    id SERIAL PRIMARY KEY,
                    anio INTEGER NOT NULL,
                    periodo VARCHAR(10) NOT NULL,
                    UNIQUE (anio, periodo)
                );
            """)

            # 11. SEDES
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sedes (
                    id SERIAL PRIMARY KEY,
                    nombre_sede VARCHAR(100) NOT NULL UNIQUE,
                    direccion TEXT
                );
            """)

            # 12. ÁREAS
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS areas (
                    id SERIAL PRIMARY KEY,
                    nombre_area VARCHAR(100) NOT NULL UNIQUE
                );
            """)

            # 13. NOTAS DE POSTULACIÓN (ETAPA: POSTULACIÓN)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notas_postulacion (
                    id SERIAL PRIMARY KEY,
                    usuario_id INTEGER NOT NULL
                        REFERENCES usuarios(id) ON DELETE CASCADE,
                    carrera_id INTEGER NOT NULL
                        REFERENCES datos_carreras(id) ON DELETE CASCADE,
                    periodo_id INTEGER NOT NULL
                        REFERENCES periodos(id) ON DELETE CASCADE,
                    nota DECIMAL(5,2) NOT NULL CHECK (nota >= 0 AND nota <= 1000),
                    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE (usuario_id, carrera_id, periodo_id)
                );
            """)

            # 14. VERIFICACIÓN DE REGISTRO NACIONAL
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS verificacion_registro_nacional (
                    id SERIAL PRIMARY KEY,
                    usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
                    periodo_id INTEGER NOT NULL REFERENCES periodos(id) ON DELETE CASCADE,
                    verificado VARCHAR(20) NOT NULL CHECK (verificado IN ('SI', 'NO', 'EN_PROCESO')),
                    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    fecha_verificacion TIMESTAMP,
                    UNIQUE (usuario_id, periodo_id)
                );
            """)

            conn.commit()
            print("Tablas del sistema SIPU creadas correctamente")

        except Exception as e:
            conn.rollback()
            print(f"Error al crear las tablas: {e}")

        finally:
            cursor.close()
            conn.close()