from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

oferta_academica_bp = Blueprint('oferta_academica', __name__)

# --- 1. OBTENER TODOS (GET) ---
@oferta_academica_bp.route('/obtener/oferta-academica', methods=['GET'])
def obtener_oferta_academica():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("""
            SELECT
                oa.id AS id_oferta,
                c.nombre_carrera AS carrera,
                f.nombre_facultad AS facultad,
                d.nombre_duracion AS duracion,
                j.nombre_jornada AS jornada,
                m.nombre AS modalidad,
                p.nombre_periodo AS periodo,
                s.nombre_sede AS sede,
                tc.nombre_tipo AS tipo_cupo,
                oa.total_cupos
            FROM oferta_academica oa
            JOIN carreras c ON oa.carrera_id = c.id
            JOIN facultades f ON c.id_facultad = f.id
            JOIN duracion_carreras d ON c.id_duracion_carrera = d.id
            JOIN jornadas_academicas j ON oa.jornada_id = j.id
            JOIN modalidad m ON oa.modalidad_id = m.id
            JOIN periodos p ON oa.periodo_id = p.id
            JOIN sedes s ON oa.sede_id = s.id
            JOIN tipo_cupo tc ON oa.tipo_cupo_id = tc.id
            ORDER BY oa.id ASC;
        """)

        resultado = cur.fetchall()

        cur.close()
        conn.close()

        return jsonify(resultado)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

#OBTENER OFERTA ACADEMICA POR ID
@oferta_academica_bp.route('/oferta-academica/<int:id>', methods=['GET'])
def obtener_oferta_academica_id(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM oferta_academica WHERE id = %s', (id,))
    resultado = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(resultado)

#ENVIAR OFERTAS ACADEMICAS (POST) 
@oferta_academica_bp.route('/oferta-academica', methods=['POST'])
def crear_oferta_academica():
    datos = request.json
    carrera_id = datos.get('carrera_id')
    jornada_id = datos.get('jornada_id')
    modalidad_id = datos.get('modalidad_id')
    periodo_id = datos.get('periodo_id')
    sede_id = datos.get('sede_id')
    tipo_cupo_id = datos.get('tipo_cupo_id')
    total_cupos = datos.get('total_cupos')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
        
    # SQL Actualizado con los nuevos campos
    sql = """
        INSERT INTO oferta_academica 
            (carrera_id, jornada_id, modalidad_id, periodo_id, sede_id, tipo_cupo_id, total_cupos) 
            VALUES (%s, %s, %s, %s, %s, %s, %s) 
            RETURNING *
        """
        
    cur.execute(sql, (carrera_id, jornada_id, modalidad_id,periodo_id,sede_id, tipo_cupo_id, total_cupos))
        
    nueva_oferta_academica = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
        
    return jsonify(nueva_oferta_academica), 201

