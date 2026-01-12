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
            
            # 2. NACIONALIDAD
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS nacionalidad (
                    id SERIAL PRIMARY KEY,
                    nombre_nacionalidad VARCHAR(50) NOT NULL UNIQUE 
                );
            """)
            
            # 3. ESTADO CIVIL
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS estado_civil (
                    id SERIAL PRIMARY KEY,
                    nombre_estado_civil VARCHAR(20) NOT NULL UNIQUE 
                );
            """)
            
            # 4. SEXO
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sexo (
                    id SERIAL PRIMARY KEY,
                    nombre_sexo VARCHAR(10) NOT NULL UNIQUE 
                );
            """)
            # 5. PAÍS 
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pais (
                    id SERIAL PRIMARY KEY,
                    nombre_pais VARCHAR(50) NOT NULL UNIQUE 
                );
            """)
            # 6. PROVINCIA 
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS provincia (
                    id SERIAL PRIMARY KEY,
                    pais_id INTEGER NOT NULL REFERENCES pais(id),
                    nombre_provincia VARCHAR(50) NOT NULL UNIQUE 
                );
            """)
            # 7. CIUDAD 
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ciudad (
                    id SERIAL PRIMARY KEY,
                    provincia_id INTEGER NOT NULL REFERENCES provincia(id),
                    nombre_ciudad VARCHAR(50) NOT NULL UNIQUE 
                );
            """)
            # 8. DATOS DEMOGRÁFICOS (ETAPA: INSCRIPCIÓN)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS datos_demograficos (
                    id SERIAL PRIMARY KEY,
                    usuario_id INTEGER NOT NULL REFERENCES usuarios(id),
                    nacionalidad_id INTEGER REFERENCES nacionalidad(id),
                    fecha_nacimiento DATE NOT NULL,
                    estado_civil_id INTEGER REFERENCES estado_civil(id),
                    sexo_id INTEGER REFERENCES sexo(id),
                    discapacidad VARCHAR(5) NOT NULL,
                    pais_id INTEGER REFERENCES pais(id),
                    provincia_id INTEGER REFERENCES provincia(id),
                    ciudad_id INTEGER REFERENCES ciudad(id),
                    UNIQUE (usuario_id, nacionalidad_id, estado_civil_id, sexo_id, pais_id, provincia_id, ciudad_id)
                );
            """)

            # 9. DOMICILIO (ETAPA: INSCRIPCIÓN)
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

            # 10. SERVICIOS BÁSICOS (ETAPA: INSCRIPCIÓN)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS servicios_basicos (
                    id SERIAL PRIMARY KEY,
                    usuario_id INTEGER UNIQUE NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
                    agua_potable BOOLEAN DEFAULT TRUE,
                    energia_electrica BOOLEAN DEFAULT TRUE,
                    alcantarillado BOOLEAN DEFAULT TRUE,
                    recoleccion_basura BOOLEAN DEFAULT TRUE,
                    internet BOOLEAN DEFAULT TRUE
                );
            """)
            # 11. TIPO UNIDAD EDUCATIVA
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tipo_unidad_educativa (
                    id SERIAL PRIMARY KEY,  
                    nombre_tipo VARCHAR(100) NOT NULL UNIQUE
                );
            """)
            # 12. DATOS ACADÉMICOS (ETAPA: INSCRIPCIÓN)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS datos_academicos (
                    id SERIAL PRIMARY KEY,
                    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE CASCADE,
                    titulo_homologado VARCHAR(100) ,
                    unidad_educativa VARCHAR(150) NOT NULL,
                    tipo_unidad_educativa_id VARCHAR(50) NOT NULL,
                    calificacion DECIMAL(5,2) NOT NULL,
                    cuadro_honor VARCHAR(5) ,
                    titulo_tercer_nivel VARCHAR(150) ,
                    titulo_cuarto_nivel VARCHAR(150) ,
                    fecha_registro_nacional DATE NOT NULL
                );
            """)

            # 13. MODALIDAD
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS modalidad (
                    id SERIAL PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL UNIQUE
                );
            """)

            # 14. DURACIÓN DE CARRERAS
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS duracion_carreras (
                    id SERIAL PRIMARY KEY,
                    nombre_duracion VARCHAR(3) NOT NULL UNIQUE
                );
            """)

            # 15. FACULTADES 
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS facultades (
                    id SERIAL PRIMARY KEY,
                    nombre_facultad VARCHAR(500) NOT NULL UNIQUE,
                    abreviacion VARCHAR(20) NOT NULL UNIQUE
                );
            """)

            # 16. CARRERAS (ETAPA: POSTULACIÓN)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS carreras (
                    id SERIAL PRIMARY KEY,
                    nombre_carrera VARCHAR(150) NOT NULL UNIQUE,
                    id_duracion_carrera INTEGER NOT NULL REFERENCES duracion_carreras(id),
                    id_facultad INTEGER NOT NULL REFERENCES facultades(id)         
                );
            """)
            
            # 17. JORNADAS ACADÉMICAS
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS jornadas_academicas (
                    id SERIAL PRIMARY KEY,
                    nombre_jornada VARCHAR(50) NOT NULL UNIQUE
                );
            """)

            # 18. PERÍODOS ACADÉMICOS
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS periodos (
                    id SERIAL PRIMARY KEY,
                    nombre_periodo VARCHAR(10) NOT NULL,
                    UNIQUE (nombre_periodo)
                );
            """)

            # 19. SEDES
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sedes (
                    id SERIAL PRIMARY KEY,
                    nombre_sede VARCHAR(100) NOT NULL UNIQUE
                );
            """)

            # 20. ÁREAS
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS areas (
                    id SERIAL PRIMARY KEY,
                    nombre_area VARCHAR(100) NOT NULL UNIQUE
                );
            """)

            # 21. POSTULACIÓN
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notas_postulacion (
                    id SERIAL PRIMARY KEY,
                    usuario_id INTEGER NOT NULL
                        REFERENCES usuarios(id) ON DELETE CASCADE,
                    carrera_id INTEGER NOT NULL
                        REFERENCES datos_carreras(id) ON DELETE CASCADE,
                    periodo_id INTEGER NOT NULL
                        REFERENCES periodos(id) ON DELETE CASCADE,
                    nota INTEGER DEFAULT (FLOOR (300 + RANDOM() * 701)),
                    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE (usuario_id, carrera_id, periodo_id)
                );
            """)

            # 22. VERIFICACIÓN DE REGISTRO NACIONAL
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

            # 23. TIPO DE CUPO
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tipo_cupo (
                    id SERIAL PRIMARY KEY,
                    nombre_tipo VARCHAR(20) NOT NULL UNIQUE
                );
            """)

<<<<<<< HEAD
            # 24. OFERTA ACADEMICA
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS oferta_academica (
                    id SERIAL PRIMARY KEY,
                    carrera_id INTEGER NOT NULL REFERENCES carreras(id) ON DELETE CASCADE,
                    jornada_id INTEGER NOT NULL REFERENCES jornadas_academicas(id) ON DELETE CASCADE,
                    modalidad_id INTEGER NOT NULL REFERENCES modalidad(id) ON DELETE CASCADE,
                    periodo_id INTEGER NOT NULL REFERENCES periodos(id) ON DELETE CASCADE,
                    sede_id INTEGER NOT NULL REFERENCES sedes(id) ON DELETE CASCADE,
                    tipo_cupo_id INTEGER NOT NULL REFERENCES tipo_cupo(id) ON DELETE CASCADE,
                    total_cupos VARCHAR(4) NOT NULL,
                    UNIQUE (carrera_id, jornada_id, modalidad_id, tipo_cupo_id, periodo_id, sede_id)
                );
            """)
            # 25. BLOQUE
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS bloque (
                    id SERIAL PRIMARY KEY,
                    nombre_bloque VARCHAR(20) NOT NULL UNIQUE
                );
            """)
            # 26. SALA
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sala (
                    id SERIAL PRIMARY KEY,
                    nombre_sala VARCHAR(20) NOT NULL UNIQUE
                );
            """)
            # 27. SEDE EVALUACION
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sede_evaluacion (
                    id SERIAL PRIMARY KEY,
                    usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
                    sede_id INTEGER NOT NULL REFERENCES sedes(id) ON DELETE CASCADE,
                    bloque_id INTEGER NOT NULL REFERENCES bloque(id) ON DELETE CASCADE,
                    sala_id INTEGER NOT NULL REFERENCES sala(id) ON DELETE CASCADE,
                    fecha_evaluacion TIMESTAMP NOT NULL,
                    hora_evaluacion TIME NOT NULL,
                    estado BOOLEAN NOT NULL DEFAULT true,
                    nombre_tipo VARCHAR(20) NOT NULL UNIQUE
                );
            """)
            # 28. INSCRPCION
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS inscripcion (
                    id SERIAL PRIMARY KEY,
                    usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
                    oferta_academica_id INTEGER NOT NULL REFERENCES oferta_academica(id) ON DELETE CASCADE,
                    numero_intencion VARCHAR(2) DEFAULT '1',
                    UNIQUE (usuario_id, oferta_academica_id)
                );
            """)
           
=======
            # 17. Inscripcion 
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS datos_inscripcion (
                    id SERIAL PRIMARY KEY,
                    usuario_id INTEGER NOT NULL
                    REFERENCES usuarios(id) ON DELETE CASCADE,
                    periodo_id INTEGER NOT NULL
                    REFERENCES periodos(id) ON DELETE CASCADE,
                    carrera_id INTEGER NOT NULL
                    REFERENCES datos_carreras(id) ON DELETE CASCADE,
                    sede_id INTEGER NOT NULL
                    REFERENCES sedes(id),
                    numero_intencion INTEGER DEFAULT 1,
                    fecha_inscripcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE (usuario_id, periodo_id)
                );
            """)

>>>>>>> 3f51995a21a6ae940aba8f16aacfdf6357971860
            conn.commit()
            print("Tablas del sistema SIPU creadas correctamente")

        except Exception as e:
            conn.rollback()
            print(f"Error al crear las tablas: {e}")

        finally:
            cursor.close()
            conn.close()