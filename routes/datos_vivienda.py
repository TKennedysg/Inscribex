from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import jwt_required, get_jwt_identity

vivienda_bp = Blueprint('vivienda', __name__)

# --- 1. OBTENER VIVIENDAS (GET) ---
@vivienda_bp.route('/viviendas', methods=['GET'])
def obtener_viviendas():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # 👇 TABLA CORRECTA
    cur.execute('SELECT * FROM domicilio')
    resultado = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify(resultado)


# --- 2. CREAR VIVIENDA (POST) ---
@vivienda_bp.route('/viviendas', methods=['POST'])
def crear_vivienda():
    datos = request.json

    usuario_id = datos.get('usuario_id')
    barrio = datos.get('barrio')
    calle_principal = datos.get('calle_principal')
    calle_secundaria = datos.get('calle_secundaria')
    numero_domicilio = datos.get('numero_domicilio')
    tipo_vivienda = datos.get('tipo_vivienda')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        """
        INSERT INTO domicilio (
            usuario_id,
            barrio,
            calle_principal,
            calle_secundaria,
            numero_domicilio,
            tipo_vivienda
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING *
        """,
        (
            usuario_id,
            barrio,
            calle_principal,
            calle_secundaria,
            numero_domicilio,
            tipo_vivienda
        )
    )

    nuevo_registro = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(nuevo_registro), 201


# -----------------------------
# 3. ACTUALIZAR DOMICILIO (PUT)
# -----------------------------
@vivienda_bp.route('/viviendas/<int:id>', methods=['PUT'])
def actualizar_vivienda(id):
    datos = request.json

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        """
        UPDATE domicilio
        SET barrio = %s,
            calle_principal = %s,
            calle_secundaria = %s,
            numero_domicilio = %s,
            tipo_vivienda = %s
        WHERE id = %s
        RETURNING *
        """,
        (
            datos.get('barrio'),
            datos.get('calle_principal'),
            datos.get('calle_secundaria'),
            datos.get('numero_domicilio'),
            datos.get('tipo_vivienda'),
            id
        )
    )

    domicilio_actualizado = cur.fetchone()

    if domicilio_actualizado is None:
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Domicilio no encontrado"}), 404

    conn.commit()
    cur.close()
    conn.close()

    return jsonify(domicilio_actualizado)


# -----------------------------
# 4. ELIMINAR DOMICILIO (DELETE)
# -----------------------------
@vivienda_bp.route('/viviendas/<int:id>', methods=['DELETE'])
def eliminar_vivienda(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        'DELETE FROM domicilio WHERE id = %s RETURNING *',
        (id,)
    )

    domicilio_eliminado = cur.fetchone()

    if domicilio_eliminado is None:
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Domicilio no encontrado"}), 404

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"mensaje": f"Domicilio con ID {id} eliminado correctamente"}), 200


    # obtener informacion mediante jwtoken
@vivienda_bp.route('/domicilio', methods=['GET'])
@jwt_required()
def obtener_mi_domicilio():
    try:
        # ID del usuario desde el JWT
        usuario_id = get_jwt_identity()

        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        query = """
            SELECT
                id,
                barrio,
                calle_principal,
                calle_secundaria,
                numero_domicilio,
                tipo_vivienda
            FROM domicilio
            WHERE usuario_id = %s
        """

        cur.execute(query, (usuario_id,))
        domicilio = cur.fetchone()

        cur.close()
        conn.close()

        if domicilio:
            return jsonify(domicilio), 200
        else:
            return jsonify({"mensaje": "Domicilio no registrado"}), 404

    except Exception as e:
        print("Error al obtener domicilio:", e)
        return jsonify({"error": str(e)}), 500