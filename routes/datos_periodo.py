from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

periodos_bp = Blueprint('periodos', __name__)

# --- 1. OBTENER PERÍODOS (GET) ---
@periodos_bp.route('/obtener/periodos', methods=['GET'])
def obtener_periodos():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("SELECT * FROM periodos ORDER BY nombre_periodo")
    resultado = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify(resultado)


# --- 2. CREAR PERÍODO (POST) ---
@periodos_bp.route('/periodos', methods=['POST'])
def crear_periodo():
    datos = request.json

    nombre_periodo = datos.get('nombre_periodo')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        """
        INSERT INTO periodos (nombre_periodo)
        VALUES (%s)
        RETURNING *
        """,
        (nombre_periodo,)
    )

    nuevo_periodo = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(nuevo_periodo), 201


# --- 3. ACTUALIZAR PERÍODO (PUT) ---
@periodos_bp.route('/periodos/<int:id>', methods=['PUT'])
def actualizar_periodo(id):
    datos = request.json

    nombre_periodo = datos.get('nombre_periodo')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        """
        UPDATE periodos
        SET nombre_periodo = %s
        WHERE id = %s
        RETURNING *
        """,
        (nombre_periodo, id)
    )

    periodo_actualizado = cur.fetchone()

    if periodo_actualizado is None:
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Período no encontrado"}), 404

    conn.commit()
    cur.close()
    conn.close()

    return jsonify(periodo_actualizado)


# --- 4. ELIMINAR PERÍODO (DELETE) ---
@periodos_bp.route('/periodos/<int:id>', methods=['DELETE'])
def eliminar_periodo(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM periodos WHERE id = %s RETURNING *",
        (id,)
    )

    eliminado = cur.fetchone()

    if eliminado is None:
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Período no encontrado"}), 404

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"mensaje": f"Período con ID {id} eliminado correctamente"}), 200
