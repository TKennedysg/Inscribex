from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

duracion_carreras_bp = Blueprint('duracion_carreras', __name__)

#OBTENER DURACION CARRERAS GET
@duracion_carreras_bp.route('/obtener/duracion-carreras', methods=['GET'])
def obtener_duracion_carreras():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM duracion_carreras')
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(resultado)

#CREAR DURACION CARRERA POST
@duracion_carreras_bp.route('/duracion-carreras', methods=['POST'])
def crear_duracion_carrera():
    datos = request.json
    nombre_duracion = datos.get('nombre_duracion')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        '''
        INSERT INTO duracion_carreras (nombre_duracion)
        VALUES (%s)
        RETURNING *
        ''',
        (nombre_duracion,)
    )

    nueva_duracion = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(nueva_duracion), 201

#ACTUALIZAR DURACION CARRERA PUT
@duracion_carreras_bp.route('/duracion-carreras/<int:id>', methods=['PUT'])
def actualizar_duracion_carrera(id):
    datos = request.json
    nombre_duracion = datos.get('nombre_duracion')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        '''
        UPDATE duracion_carreras
        SET nombre_duracion = %s
        WHERE id = %s
        RETURNING *
        ''',
        (nombre_duracion, id)
    )

    duracion_actualizada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(duracion_actualizada)

#ELIMINAR DURACION CARRERA DELETE
@duracion_carreras_bp.route('/duracion-carreras/<int:id>', methods=['DELETE'])
def eliminar_duracion_carrera(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        'DELETE FROM duracion_carreras WHERE id = %s RETURNING *',
        (id,)
    )

    duracion_eliminada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(duracion_eliminada), 200
