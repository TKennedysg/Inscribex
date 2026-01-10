from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

verificacion_bp = Blueprint('verificacion_registro_nacional', __name__)

# --- 1. OBTENER REGISTROS DE VERIFICACIÓN (GET) ---
@verificacion_bp.route('/verificacion-registro-nacional', methods=['GET'])
def obtener_verificaciones():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""
        SELECT *
        FROM verificacion_registro_nacional
        ORDER BY fecha_creacion DESC
    """)

    resultado = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(resultado)


# --- 2. CREAR REGISTRO DE VERIFICACIÓN (POST) ---
@verificacion_bp.route('/verificacion-registro-nacional', methods=['POST'])
def crear_verificacion():
    datos = request.json

    usuario_id = datos.get('usuario_id')
    periodo_id = datos.get('periodo_id')
    verificado = datos.get('verificado')  # SI | NO | EN_PROCESO

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        """
        INSERT INTO verificacion_registro_nacional (
            usuario_id,
            periodo_id,
            verificado
        )
        VALUES (%s, %s, %s)
        RETURNING *
        """,
        (usuario_id, periodo_id, verificado)
    )

    nuevo_registro = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(nuevo_registro), 201


# --- 3. ACTUALIZAR VERIFICACIÓN (PUT) ---
@verificacion_bp.route('/verificacion-registro-nacional/<int:id>', methods=['PUT'])
def actualizar_verificacion(id):
    datos = request.json

    verificado = datos.get('verificado')
    fecha_verificacion = datos.get('fecha_verificacion')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        """
        UPDATE verificacion_registro_nacional
        SET
            verificado = %s,
            fecha_verificacion = %s
        WHERE id = %s
        RETURNING *
        """,
        (verificado, fecha_verificacion, id)
    )

    registro_actualizado = cur.fetchone()

    if registro_actualizado is None:
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Registro de verificación no encontrado"}), 404

    conn.commit()
    cur.close()
    conn.close()

    return jsonify(registro_actualizado)


# --- 4. ELIMINAR REGISTRO DE VERIFICACIÓN (DELETE) ---
@verificacion_bp.route('/verificacion-registro-nacional/<int:id>', methods=['DELETE'])
def eliminar_verificacion(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        DELETE FROM verificacion_registro_nacional
        WHERE id = %s
        RETURNING *
        """,
        (id,)
    )

    eliminado = cur.fetchone()

    if eliminado is None:
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Registro de verificación no encontrado"}), 404

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"mensaje": f"Registro de verificación con ID {id} eliminado correctamente"}), 200
