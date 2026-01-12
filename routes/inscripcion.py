from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import jwt_required, get_jwt_identity

inscripcion_bp = Blueprint('inscripcion', __name__)

<<<<<<< HEAD
# --- 1. OBTENER TODOS (GET) ---
@inscripcion_bp.route('/obtener/inscripciones', methods=['GET'])
def obtener_inscripcion():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM inscripcion ORDER BY id ASC') # Agregué orden
        resultado = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    # obtener inscripcion por id (ADMINISTRADOR)

@inscripcion_bp.route('/inscripcion/<int:id>', methods=['GET'])
def obtener_inscripcion_id(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM inscripcion WHERE id = %s', (id,))
    resultado = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(resultado)

# CREAR INSCRIPCION (POST) 
@inscripcion_bp.route('/inscripcion', methods=['POST'])
def crear_inscripcion():
    datos = request.json
    usuario_id = datos.get('usuario_id')
    oferta_academica_id = datos.get('oferta_academica_id')
    numero_intencion = datos.get('numero_intencion')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
        
    # SQL Actualizado con los nuevos campos
    sql = """
        INSERT INTO inscripcion 
            (usuario_id, oferta_academica_id, numero_intencion) 
            VALUES (%s, %s, %s) 
            RETURNING *
        """
        
    cur.execute(sql, (usuario_id, oferta_academica_id, numero_intencion))
        
    nueva_inscripcion = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
        
    return jsonify(nueva_inscripcion), 201

=======
@inscripcion_bp.route('/inscripcion', methods=['GET'])
@jwt_required()
def obtener_mi_inscripcion():
    usuario_id = get_jwt_identity()

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""
        SELECT *
        FROM inscripcion
        WHERE usuario_id = %s
    """, (usuario_id,))

    inscripcion = cur.fetchone()

    cur.close()
    conn.close()

    if inscripcion:
        return jsonify(inscripcion), 200
    else:
        return jsonify({"mensaje": "El usuario aún no tiene inscripción"}), 404


@inscripcion_bp.route('/inscripcion', methods=['POST'])
@jwt_required()
def crear_inscripcion():
    usuario_id = get_jwt_identity()
    datos = request.json

    periodo_id = datos.get('periodo_id')
    carrera_id = datos.get('carrera_id')
    sede_id = datos.get('sede_id')
    numero_intencion = datos.get('numero_intencion', 1)

    if not periodo_id or not carrera_id or not sede_id:
        return jsonify({"mensaje": "Todos los campos son obligatorios"}), 400

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute("""
            INSERT INTO inscripcion (
                usuario_id,
                periodo_id,
                carrera_id,
                sede_id,
                numero_intencion
            )
            VALUES (%s, %s, %s, %s, %s)
            RETURNING *
        """, (
            usuario_id,
            periodo_id,
            carrera_id,
            sede_id,
            numero_intencion
        ))

        nueva_inscripcion = cur.fetchone()
        conn.commit()

        return jsonify({
            "mensaje": "Inscripción creada correctamente",
            "inscripcion": nueva_inscripcion
        }), 201

    except Exception as e:
        conn.rollback()
        if "unique" in str(e).lower():
            return jsonify({"mensaje": "Ya existe una inscripción para este período"}), 409
        return jsonify({"error": str(e)}), 500

    finally:
        cur.close()
        conn.close()


@inscripcion_bp.route('/inscripcion', methods=['PUT'])
@jwt_required()
def actualizar_inscripcion():
    usuario_id = get_jwt_identity()
    datos = request.json

    campos_permitidos = ['carrera_id', 'sede_id', 'numero_intencion']
    partes_sql = []
    valores = []

    for campo in campos_permitidos:
        if campo in datos:
            partes_sql.append(f"{campo} = %s")
            valores.append(datos[campo])

    if not partes_sql:
        return jsonify({"mensaje": "No hay datos para actualizar"}), 400

    valores.append(usuario_id)

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        query = f"""
            UPDATE inscripcion
            SET {', '.join(partes_sql)}
            WHERE usuario_id = %s
            RETURNING *
        """
        cur.execute(query, tuple(valores))
        inscripcion_actualizada = cur.fetchone()

        if not inscripcion_actualizada:
            return jsonify({"mensaje": "Inscripción no encontrada"}), 404

        conn.commit()
        return jsonify({
            "mensaje": "Inscripción actualizada correctamente",
            "inscripcion": inscripcion_actualizada
        }), 200

    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        cur.close()
        conn.close()
>>>>>>> 3f51995a21a6ae940aba8f16aacfdf6357971860
