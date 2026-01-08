from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

areas_bp = Blueprint('areas', __name__)

# --- OBTENER TODAS LAS AREAS (GET) ---
@areas_bp.route('/areas', methods=['GET'])
def obtener_areas():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute('SELECT * FROM areas')
    resultado = cur.fetchall()
    
    cur.close()
    conn.close()
    return jsonify(resultado)


# --- CREAR UNA NUEVA AREA (POST) ---
@areas_bp.route('/areas', methods=['POST'])
def crear_area():
    datos = request.json
    nombre_area = datos.get('nombre_area')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute(
            '''
            INSERT INTO areas (nombre_area)
            VALUES (%s)
            RETURNING *
            ''',
            (nombre_area,)
        )
        nueva_area = cur.fetchone()
        conn.commit()
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 400
    finally:
        cur.close()
        conn.close()

    return jsonify(nueva_area), 201


# --- ACTUALIZAR UN AREA (PUT) ---
@areas_bp.route('/areas/<int:id>', methods=['PUT'])
def actualizar_area(id):
    datos = request.json
    nombre_area = datos.get('nombre_area')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        '''
        UPDATE areas
        SET nombre_area = %s
        WHERE id = %s
        RETURNING *
        ''',
        (nombre_area, id)
    )

    area_actualizada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if area_actualizada is None:
        return jsonify({'mensaje': 'Area no encontrada'}), 404

    return jsonify(area_actualizada)


# --- ELIMINAR UN AREA (DELETE) ---
@areas_bp.route('/areas/<int:id>', methods=['DELETE'])
def eliminar_area(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        'DELETE FROM areas WHERE id = %s RETURNING *',
        (id,)
    )

    area_eliminada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if area_eliminada is None:
        return jsonify({'mensaje': 'Area no encontrada'}), 404

    return jsonify(area_eliminada), 200