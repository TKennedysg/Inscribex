from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

jornadas_academicas_bp = Blueprint('jornadas_academicas', __name__)

# --- OBTENER TODAS LAS JORNADAS (GET) ---
@jornadas_academicas_bp.route('/jornadas-academicas', methods=['GET'])
def obtener_jornadas():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute('SELECT * FROM jornadas_academicas')
    resultado = cur.fetchall()
    
    cur.close()
    conn.close()
    return jsonify(resultado)


# --- CREAR UNA NUEVA JORNADA (POST) ---
@jornadas_academicas_bp.route('/jornadas-academicas', methods=['POST'])
def crear_jornada():
    datos = request.json
    nombre_jornada = datos.get('nombre_jornada')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        '''
        INSERT INTO jornadas_academicas (nombre_jornada)
        VALUES (%s)
        RETURNING *
        ''',
        (nombre_jornada,)
    )

    nueva_jornada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(nueva_jornada), 201


# --- ACTUALIZAR UNA JORNADA (PUT) ---
@jornadas_academicas_bp.route('/jornadas-academicas/<int:id>', methods=['PUT'])
def actualizar_jornada(id):
    datos = request.json
    nombre_jornada = datos.get('nombre_jornada')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        '''
        UPDATE jornadas_academicas
        SET nombre_jornada = %s
        WHERE id = %s
        RETURNING *
        ''',
        (nombre_jornada, id)
    )

    jornada_actualizada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if jornada_actualizada is None:
        return jsonify({'mensaje': 'Jornada no encontrada'}), 404

    return jsonify(jornada_actualizada)


# --- ELIMINAR UNA JORNADA (DELETE) ---
@jornadas_academicas_bp.route('/jornadas-academicas/<int:id>', methods=['DELETE'])
def eliminar_jornada(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        'DELETE FROM jornadas_academicas WHERE id = %s RETURNING *',
        (id,)
    )

    jornada_eliminada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if jornada_eliminada is None:
        return jsonify({'mensaje': 'Jornada no encontrada'}), 404

    return jsonify(jornada_eliminada), 200