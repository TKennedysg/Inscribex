from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

datos_demograficos_bp = Blueprint('datos_demograficos', __name__)

# --- 1. OBTENER TODOS (GET) ---
@datos_demograficos_bp.route('/datos-demograficos', methods=['GET'])
def obtener_datos_demograficos():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("""
            SELECT * 
            FROM datos_demograficos 
            ORDER BY id ASC
        """)

        resultado = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(resultado)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- 2. CREAR DATOS DEMOGRÁFICOS (POST) ---
@datos_demograficos_bp.route('/datos-demograficos', methods=['POST'])
def crear_datos_demograficos():
    datos = request.json

    usuario_id = datos.get('usuario_id')
    nacionalidad = datos.get('nacionalidad')
    fecha_nacimiento = datos.get('fecha_nacimiento')
    estado_civil = datos.get('estado_civil')
    sexo = datos.get('sexo')
    autoidentificacion = datos.get('autoidentificacion')
    discapacidad = datos.get('discapacidad')
    pais = datos.get('pais')
    provincia = datos.get('provincia')
    ciudad = datos.get('ciudad')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    sql = """
        INSERT INTO datos_demograficos (
            usuario_id,
            nacionalidad,
            fecha_nacimiento,
            estado_civil,
            sexo,
            autoidentificacion,
            discapacidad,
            pais,
            provincia,
            ciudad
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING *
    """

    try:
        cur.execute(sql, (
            usuario_id,
            nacionalidad,
            fecha_nacimiento,
            estado_civil,
            sexo,
            autoidentificacion,
            discapacidad,
            pais,
            provincia,
            ciudad
        ))

        nuevo_registro = cur.fetchone()
        conn.commit()

    except Exception as e:
        conn.rollback()
        cur.close()
        conn.close()
        return jsonify({"error": str(e)}), 500

    cur.close()
    conn.close()
    return jsonify(nuevo_registro), 201


# --- 3. ACTUALIZAR DATOS DEMOGRÁFICOS (PUT) ---
@datos_demograficos_bp.route('/datos-demograficos/<int:id>', methods=['PUT'])
def actualizar_datos_demograficos(id):
    datos = request.json

    nacionalidad = datos.get('nacionalidad')
    fecha_nacimiento = datos.get('fecha_nacimiento')
    estado_civil = datos.get('estado_civil')
    sexo = datos.get('sexo')
    autoidentificacion = datos.get('autoidentificacion')
    discapacidad = datos.get('discapacidad')
    pais = datos.get('pais')
    provincia = datos.get('provincia')
    ciudad = datos.get('ciudad')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    sql = """
        UPDATE datos_demograficos
        SET nacionalidad = %s,
            fecha_nacimiento = %s,
            estado_civil = %s,
            sexo = %s,
            autoidentificacion = %s,
            discapacidad = %s,
            pais = %s,
            provincia = %s,
            ciudad = %s
        WHERE id = %s
        RETURNING *
    """

    try:
        cur.execute(sql, (
            nacionalidad,
            fecha_nacimiento,
            estado_civil,
            sexo,
            autoidentificacion,
            discapacidad,
            pais,
            provincia,
            ciudad,
            id
        ))

        actualizado = cur.fetchone()
        conn.commit()

    except Exception as e:
        conn.rollback()
        cur.close()
        conn.close()
        return jsonify({"error": str(e)}), 500

    cur.close()
    conn.close()

    if actualizado is None:
        return jsonify({"mensaje": "Registro no encontrado"}), 404

    return jsonify(actualizado)


# --- 4. ELIMINAR DATOS DEMOGRÁFICOS (DELETE) ---
@datos_demograficos_bp.route('/datos-demograficos/<int:id>', methods=['DELETE'])
def eliminar_datos_demograficos(id):
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "DELETE FROM datos_demograficos WHERE id = %s RETURNING id",
            (id,)
        )
        eliminado = cur.fetchone()
        conn.commit()

    except Exception as e:
        conn.rollback()
        cur.close()
        conn.close()
        return jsonify({"error": str(e)}), 500

    cur.close()
    conn.close()

    if eliminado is None:
        return jsonify({"mensaje": "Registro no encontrado"}), 404

    return jsonify({"mensaje": f"Datos demográficos con ID {id} eliminados correctamente"}), 200
