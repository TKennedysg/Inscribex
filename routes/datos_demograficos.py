from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from flask_jwt_extended import jwt_required, get_jwt_identity
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



# ACTUALIZAR MI PERFIL (PUT) 
@datos_demograficos_bp.route('/datos-demograficos/actualizar', methods=['PUT'])
@jwt_required()
def actualizar_datos_demograficos_jwt():
    # 1. Extraemos el ID directamente del TOKEN (Seguridad total)
    usuario_id = get_jwt_identity()
    
    datos = request.json
    if not datos:
        return jsonify({"mensaje": "No hay datos para actualizar"}), 400

    # Campos que el propio usuario tiene permiso de cambiar
    campos_permitidos = ['nacionalidad', 'fecha_nacimiento', 'estado_civil', 'sexo', 'autoidentificacion', 'discapacidad', 'pais', 'provincia', 'ciudad']
    partes_sql = []
    valores = []

    for campo in campos_permitidos:
        if campo in datos:
            partes_sql.append(f"{campo} = %s")
            valores.append(datos[campo])

    if not partes_sql:
        return jsonify({"mensaje": "Nada que actualizar"}), 400

    valores.append(usuario_id) # El ID viene del token, no de la URL

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    try:
        query = f"UPDATE datos_demograficos SET {', '.join(partes_sql)} WHERE id = %s RETURNING id, nacionalidad, fecha_nacimiento, estado_civil, sexo, autoidentificacion, discapacidad, pais, provincia, ciudad"
        cur.execute(query, tuple(valores))
        datos_actualizados = cur.fetchone()
        conn.commit()
        
        return jsonify({
            "mensaje": "Los datos de tu perfil han sido actualizado",
            "usuario": datos_actualizados
        })
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
        conn.close()


# obtener informacion mediante jwtoken
@datos_demograficos_bp.route('/datos-demograficos', methods=['GET'])
@jwt_required()
def obtener_datos_demograficos_jwt():
    try:
        # Extrae el ID que guardamos en el login (identity)
        usuario_id = get_jwt_identity() 
        
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Aprovechamos para traer sus datos académicos con un JOIN
        cur.execute('SELECT * FROM datos_demograficos WHERE id = %s', (usuario_id,))
        
        datos_demograficos = cur.fetchone()
        
        cur.close()
        conn.close()

        if datos_demograficos:
            datos_demograficos.pop('usuario_id', None)
            return jsonify(datos_demograficos), 200
        else:
            return jsonify({"mensaje": "Datos demograficos no encontrado"}), 404

    except Exception as e:
        print(f"Error al obtener datos demograficos: {e}")
        return jsonify({"error": str(e)}), 500
    
#CREAR DATOS DEMOGRAFICOS
@datos_demograficos_bp.route('/datos-demograficos/nuevo', methods=['POST'])
@jwt_required()
def crear_datos_demograficos_jwt():
    # 1. Obtenemos el ID del usuario desde el token
    usuario_id = get_jwt_identity()
    datos = request.json

    # 2. Validación de campos requeridos (según tu esquema NOT NULL)
    campos_requeridos = ['nacionalidad', 'fecha_nacimiento', 'estado_civil', 'sexo', 'autoidentificacion', 'discapacidad', 'pais', 'provincia', 'ciudad']
    for campo in campos_requeridos:
        if campo not in datos or datos[campo] is None:
            return jsonify({"mensaje": f"El campo {campo} es obligatorio"}), 400

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        # 3. Insertar datos
        # Nota: Usamos usuario_id como la columna de referencia
        query = """
            INSERT INTO datos_demograficos (usuario_id, nacionalidad, fecha_nacimiento, estado_civil, sexo, autoidentificacion, discapacidad, pais, provincia, ciudad)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING *
        """
        valores = (
            usuario_id, 
            datos['nacionalidad'], 
            datos['fecha_nacimiento'], 
            datos['estado_civil'], 
            datos['sexo'], 
            datos['autoidentificacion'], 
            datos['discapacidad'], 
            datos['pais'], 
            datos['provincia'], 
            datos['ciudad']
        )
        
        cur.execute(query, valores)
        nuevos_datos_demograficos = cur.fetchone()
        conn.commit()

        return jsonify({
            "mensaje": "Datos demográficos registrados exitosamente",
            "datos": nuevos_datos_demograficos
        }), 201

    except Exception as e:
        conn.rollback()
        # Manejo específico para el caso de que ya existan datos (por el UNIQUE usuario_id)
        if "already exists" in str(e).lower() or "duplicado" in str(e).lower():
            return jsonify({"mensaje": "Los datos demograficos de este usuario ya están registrados. Use PUT para actualizar."}), 409
        
        print(f"Error al crear datos demograficos: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
        conn.close()