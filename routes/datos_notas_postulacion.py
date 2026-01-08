from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

notas_postulacion_bp = Blueprint('notas_postulacion', __name__)

# --- 1. OBTENER NOTAS DE POSTULACIÓN (GET) ---
@notas_postulacion_bp.route('/notas-postulacion', methods=['GET'])
def obtener_notas_postulacion():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute('SELECT * FROM notas_postulacion')
    resultado = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify(resultado)


# --- 2. CREAR NOTA DE POSTULACIÓN (POST) ---
@notas_postulacion_bp.route('/notas-postulacion', methods=['POST'])
def crear_nota_postulacion():
    datos = request.json

    usuario_id = datos.get('usuario_id')
    carrera_id = datos.get('carrera_id')
    periodo_id = datos.get('periodo_id')
    nota = datos.get('nota')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        """
        INSERT INTO notas_postulacion (
            usuario_id,
            carrera_id,
            periodo_id,
            nota
        )
        VALUES (%s, %s, %s, %s)
        RETURNING *
        """,
        (
            usuario_id,
            carrera_id,
            periodo_id,
            nota
        )
    )

    nuevo_registro = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(nuevo_registro), 201


# --- 3. ACTUALIZAR NOTA DE POSTULACIÓN (PUT) ---
@notas_postulacion_bp.route('/notas-postulacion/<int:id>', methods=['PUT'])
def actualizar_nota_postulacion(id):
    datos = request.json

    usuario_id = datos.get('usuario_id')
    carrera_id = datos.get('carrera_id')
    periodo_id = datos.get('periodo_id')
    nota = datos.get('nota')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        """
        UPDATE notas_postulacion
        SET
            usuario_id = %s,
            carrera_id = %s,
            periodo_id = %s,
            nota = %s
        WHERE id = %s
        RETURNING *
        """,
        (
            usuario_id,
            carrera_id,
            periodo_id,
            nota,
            id
        )
    )

    registro_actualizado = cur.fetchone()

    if registro_actualizado is None:
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Nota de postulación no encontrada"}), 404

    conn.commit()
    cur.close()
    conn.close()

    return jsonify(registro_actualizado)


# --- 4. ELIMINAR NOTA DE POSTULACIÓN (DELETE) ---
@notas_postulacion_bp.route('/notas-postulacion/<int:id>', methods=['DELETE'])
def eliminar_nota_postulacion(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        'DELETE FROM notas_postulacion WHERE id = %s RETURNING *',
        (id,)
    )

    registro_eliminado = cur.fetchone()

    if registro_eliminado is None:
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Nota de postulación no encontrada"}), 404

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"mensaje": f"Nota de postulación con ID {id} eliminada correctamente"}), 200
