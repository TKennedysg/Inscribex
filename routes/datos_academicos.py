from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import jwt_required, get_jwt_identity

datos_academicos_bp = Blueprint('datos_academicos', __name__)

# --- 1. OBTENER DATOS ACADÉMICOS (GET) ---
@datos_academicos_bp.route('/datos-academicos', methods=['GET'])
def obtener_datos_academicos():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM datos_academicos')
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(resultado)


@datos_academicos_bp.route('/datos-academicos', methods=['POST'])
def crear_datos_academicos():
    datos = request.json

    usuario_id = datos.get('usuario_id')
    titulo_homologado = datos.get('titulo_homologado')
    unidad_educativa = datos.get('unidad_educativa')
    tipo_unidad_educativa_id = datos.get('tipo_unidad_educativa_id')
    calificacion = datos.get('calificacion')
    cuadro_honor = datos.get('cuadro_honor')
    titulo_tercer_nivel = datos.get('titulo_tercer_nivel')
    titulo_cuarto_nivel = datos.get('titulo_cuarto_nivel')
    fecha_registro_nacional = datos.get('fecha_registro_nacional')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        """
        INSERT INTO datos_academicos (
            usuario_id,
            titulo_homologado,
            unidad_educativa,
            tipo_unidad_educativa_id,
            calificacion,
            cuadro_honor,
            titulo_tercer_nivel,
            titulo_cuarto_nivel,
            fecha_registro_nacional
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING *
        """,
        (
            usuario_id,
            titulo_homologado,
            unidad_educativa,
            tipo_unidad_educativa_id,
            calificacion,
            cuadro_honor,
            titulo_tercer_nivel,
            titulo_cuarto_nivel,
            fecha_registro_nacional
        )
    )

    nuevo_registro = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(nuevo_registro), 201


#ACTUALIZAR DATOS ACADÉMICOS (PUT)
@datos_academicos_bp.route('/datos-academicos/<int:id>', methods=['PUT'])
def actualizar_datos_academicos(id):
    datos = request.json

    usuario_id = datos.get('usuario_id')
    titulo_homologado = datos.get('titulo_homologado')
    unidad_educativa = datos.get('unidad_educativa')
    tipo_unidad_educativa_id = datos.get('tipo_unidad_educativa_id')
    calificacion = datos.get('calificacion')
    cuadro_honor = datos.get('cuadro_honor')
    titulo_tercer_nivel = datos.get('titulo_tercer_nivel')
    titulo_cuarto_nivel = datos.get('titulo_cuarto_nivel')
    fecha_registro_nacional = datos.get('fecha_registro_nacional')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        """
        UPDATE datos_academicos
        SET
            usuario_id = %s,
            titulo_homologado = %s,
            unidad_educativa = %s,
            tipo_unidad_educativa_id = %s,
            calificacion = %s,
            cuadro_honor = %s,
            titulo_tercer_nivel = %s,
            titulo_cuarto_nivel = %s,
            fecha_registro_nacional = %s
        WHERE id = %s
        RETURNING *
        """,
        (
            usuario_id,
            titulo_homologado,
            unidad_educativa,
            tipo_unidad_educativa_id,
            calificacion,
            cuadro_honor,
            titulo_tercer_nivel,
            titulo_cuarto_nivel,
            fecha_registro_nacional,
            id
        )
    )

    registro_actualizado = cur.fetchone()

    if registro_actualizado is None:
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Registro académico no encontrado"}), 404

    conn.commit()
    cur.close()
    conn.close()

    return jsonify(registro_actualizado)



# --- 4. ELIMINAR DATOS ACADÉMICOS (DELETE) ---
@datos_academicos_bp.route('/datos-academicos/<int:id>', methods=['DELETE'])
def eliminar_datos_academicos(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        'DELETE FROM datos_academicos WHERE id = %s RETURNING *',
        (id,)
    )

    registro_eliminado = cur.fetchone()

    if registro_eliminado is None:
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Registro académico no encontrado"}), 404

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"mensaje": f"Registro académico con ID {id} eliminado correctamente"}), 200


# 5. OBTENER MIS DATOS ACADÉMICOS  MEDIANTE JWT (GET)
@datos_academicos_bp.route('/datos-academicos', methods=['GET'])
@jwt_required()
def obtener_datos_academicos_jwt():
    try:
        # ID del usuario obtenido desde el JWT
        usuario_id = get_jwt_identity()

        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        query = """
            SELECT
                id,
                titulo_homologado,
                unidad_educativa,
                tipo_unidad_educativa_id,
                calificacion,
                cuadro_honor,
                titulo_tercer_nivel,
                titulo_cuarto_nivel,
                fecha_registro_nacional
            FROM datos_academicos
            WHERE usuario_id = %s
        """

        cur.execute(query, (usuario_id,))
        datos_academicos = cur.fetchone()

        cur.close()
        conn.close()

        if datos_academicos:
            return jsonify(datos_academicos), 200
        else:
            return jsonify({"mensaje": "Datos académicos no registrados"}), 404

    except Exception as e:
        print("Error al obtener datos académicos:", e)
        return jsonify({"error": str(e)}), 500
