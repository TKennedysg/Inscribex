from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

modalidad_bp = Blueprint('modalidad', __name__)

@modalidad_bp.route('/modalidad', methods=['GET'])
def obtener_modalidades():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM modalidad')
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(resultado)


@modalidad_bp.route('/modalidad', methods=['POST'])
def crear_modalidad():
    datos = request.json
    nombre = datos.get('nombre')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        '''
        INSERT INTO modalidad (nombre)
        VALUES (%s)
        RETURNING *
        ''',
        (nombre,)
    )

    nueva_modalidad = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(nueva_modalidad), 201


@modalidad_bp.route('/modalidad/<int:id>', methods=['PUT'])
def actualizar_modalidad(id):
    datos = request.json
    nombre = datos.get('nombre')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        '''
        UPDATE modalidad
        SET nombre = %s
        WHERE id = %s
        RETURNING *
        ''',
        (nombre, id)
    )

    modalidad_actualizada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(modalidad_actualizada)


@modalidad_bp.route('/modalidad/<int:id>', methods=['DELETE'])
def eliminar_modalidad(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        'DELETE FROM modalidad WHERE id = %s RETURNING *',
        (id,)
    )

    modalidad_eliminada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(modalidad_eliminada), 200
