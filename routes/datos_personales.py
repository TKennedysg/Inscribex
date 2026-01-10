from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import jwt_required, get_jwt_identity
from storage_service import guardar_imagen_local

datos_personales_bp = Blueprint('usuarios', __name__)

# --- 1. OBTENER TODOS (GET) ---
@datos_personales_bp.route('/usuarios', methods=['GET'])
def obtener_datos_personales():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM usuarios ORDER BY id ASC') # Agregué orden
        resultado = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# obtener usuario por id (ADMINISTRADOR)

@datos_personales_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM usuarios WHERE id = %s', (id,))
    resultado = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(resultado)


# CREAR DATOS PERSONALES (POST) 
@datos_personales_bp.route('/usuarios', methods=['POST'])
def crear_datos_personales():
    datos = request.json
    nombre = datos.get('nombre')
    apellido = datos.get('apellido')
    cedula = datos.get('cedula')
    contrasena = datos.get('contrasena')
    correo = datos.get('correo') 

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
        
    # SQL Actualizado con los nuevos campos
    sql = """
        INSERT INTO usuarios 
            (nombre, apellido, cedula, contrasena, correo) 
            VALUES (%s, %s, %s, %s, %s) 
            RETURNING *
        """
        
    cur.execute(sql, (nombre, apellido, cedula, contrasena, correo))
        
    nuevo_usuario = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
        
    return jsonify(nuevo_usuario), 201
        

# ACTUALIZAR DATOS PERSONALES (PUT) 
@datos_personales_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_datos_personales(id):
    datos = request.json
    
    # Extraemos datos (usamos .get() para evitar errores si no envían un campo)
    nombre = datos.get('nombre')
    apellido = datos.get('apellido')
    cedula = datos.get('cedula')
    telefono = datos.get('telefono')
    direccion = datos.get('direccion')
    estado = datos.get('estado')


    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    # IMPORTANTE: Esta lógica asume que envías TODOS los datos en el PUT.
    # Si quieres permitir actualizaciones parciales (PATCH), la lógica SQL cambia un poco.
    
    sql = """
        UPDATE usuarios 
        SET nombre = %s, 
            apellido = %s, 
            cedula = %s,
            telefono = %s,
            direccion = %s,
            estado = %s
        WHERE id = %s 
        RETURNING *
    """
    
    try:
        cur.execute(sql, (nombre, apellido, cedula, telefono, direccion, estado, id))
        usuario_actualizado = cur.fetchone()
        conn.commit()
    except Exception as e:
        conn.rollback()
        cur.close()
        conn.close()
        return jsonify({"error": str(e)}), 500
    
    cur.close()
    conn.close()

    if usuario_actualizado is None:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    return jsonify(usuario_actualizado)


# ELIMINAR DATOS DEMOGRÁFICOS (DELETE) 
@datos_personales_bp.route('/usuario/<int:id>', methods=['DELETE'])
def eliminar_datos_demograficos(id):
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute('DELETE FROM usuario WHERE id = %s RETURNING id', (id,))
        datos_eliminados = cur.fetchone()
        conn.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
        conn.close()

    if datos_eliminados is None:
        return jsonify({"mensaje": "Datos no encontrados"}), 404

    return jsonify({"mensaje": f"Datos con ID {id} eliminados correctamente"}), 200


# ACTUALIZAR MI PERFIL (PUT) 

@datos_personales_bp.route('/perfil/actualizar', methods=['PUT'])
@jwt_required()
def actualizar_mi_perfil():
    # 1. Extraemos el ID directamente del TOKEN (Seguridad total)
    usuario_id = get_jwt_identity()
    
    datos = request.json
    if not datos:
        return jsonify({"mensaje": "No hay datos para actualizar"}), 400

    # Campos que el propio usuario tiene permiso de cambiar
    campos_permitidos = ['nombre', 'apellido', 'cedula']
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
        query = f"UPDATE usuarios SET {', '.join(partes_sql)} WHERE id = %s RETURNING id, nombre, apellido, cedula, foto_url"
        cur.execute(query, tuple(valores))
        usuario_actualizado = cur.fetchone()
        conn.commit()
        
        return jsonify({
            "mensaje": "Tu perfil ha sido actualizado",
            "usuario": usuario_actualizado
        })
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
        conn.close()


# ACTUALIZAR FOTO DE PERFIL (POST)
@datos_personales_bp.route('/perfil/foto', methods=['POST'])
@jwt_required()
def actualizar_foto_perfil():
    usuario_id = get_jwt_identity()
    
    if 'foto' not in request.files:
        return jsonify({"mensaje": "No se seleccionó ninguna imagen"}), 400
    
    foto = request.files['foto']
    
    # 1. Guardar el archivo físico
    url_relativa = guardar_imagen_local(foto)
    
    if not url_relativa:
        return jsonify({"mensaje": "Error al guardar el archivo en el disco"}), 500
    
    # 2. Guardar en Postgres
    conn = get_db_connection()
    # Usamos RealDictCursor por consistencia con tus otras rutas
    cur = conn.cursor(cursor_factory=RealDictCursor) 
    
    try:
        cur.execute(
            "UPDATE usuarios SET foto_url = %s WHERE id = %s RETURNING id",
            (url_relativa, usuario_id)
        )
        verificacion = cur.fetchone()
        
        if not verificacion:
            print(f"DEBUG: No se encontró el usuario {usuario_id} para actualizar foto")
            return jsonify({"mensaje": "Usuario no encontrado en la base de datos"}), 404

        conn.commit()
        
        # Este print aparecerá en tu terminal de Python para confirmar
        print(f"✅ Foto actualizada en DB para usuario {usuario_id}: {url_relativa}")

        return jsonify({
            "mensaje": "Foto actualizada con éxito",
            "foto_url": url_relativa
        }), 200

    except Exception as e:
        conn.rollback()
        print(f"❌ ERROR EN DB: {str(e)}") # Mira esto en tu terminal de VS Code
        return jsonify({"error": "Error interno al guardar en base de datos"}), 500
    finally:
        cur.close()
        conn.close()


# obtener informacion mediante jwtoken
@datos_personales_bp.route('/perfil', methods=['GET'])
@jwt_required()
def obtener_mi_perfil():
    try:
        # Extrae el ID que guardamos en el login (identity)
        usuario_id = get_jwt_identity() 
        
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Aprovechamos para traer sus datos académicos con un JOIN
        cur.execute('SELECT * FROM usuarios WHERE id = %s', (usuario_id,))
        
        usuario = cur.fetchone()
        
        cur.close()
        conn.close()

        if usuario:
            usuario.pop('contrasena', None)
            return jsonify(usuario), 200
        else:
            return jsonify({"mensaje": "Usuario no encontrado"}), 404

    except Exception as e:
        print(f"Error en perfil: {e}")
        return jsonify({"error": str(e)}), 500
 
