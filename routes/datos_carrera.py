from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

datos_carreras_bp = Blueprint('datos_carreras', __name__)

@datos_carreras_bp.route('/datos-carreras', methods=['GET'])
def obtener_datos_carreras():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM datos_carreras')
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(resultado)


@datos_carreras_bp.route('/datos-carreras', methods=['POST'])
def crear_datos_carreras():
    datos = request.json
    usuario_id = datos.get('usuario_id')
    id_modalidad = datos.get('id_modalidad')
    id_duracion_carrera = datos.get('id_duracion_carrera')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        '''
        INSERT INTO datos_carreras (
            usuario_id,
            id_modalidad,
            id_duracion_carrera
        ) VALUES (%s, %s, %s)
        RETURNING *
        ''',
        (
            usuario_id,
            id_modalidad,
            id_duracion_carrera
        )
    )

    nuevo_registro = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(nuevo_registro), 201


@datos_carreras_bp.route('/datos-carreras/<int:id>', methods=['PUT'])
def actualizar_datos_carreras(id):
    datos = request.json
    id_modalidad = datos.get('id_modalidad')
    id_duracion_carrera = datos.get('id_duracion_carrera')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        '''
        UPDATE datos_carreras
        SET id_modalidad = %s,
            id_duracion_carrera = %s
        WHERE id = %s
        RETURNING *
        ''',
        (
            id_modalidad,
            id_duracion_carrera,
            id
        )
    )

    registro_actualizado = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(registro_actualizado)


@datos_carreras_bp.route('/datos-carreras/<int:id>', methods=['DELETE'])
def eliminar_datos_carreras(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        'DELETE FROM datos_carreras WHERE id = %s RETURNING *',
        (id,)
    )

    registro_eliminado = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(registro_eliminado), 200
