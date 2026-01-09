from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import jwt_required, get_jwt_identity

datos_personales_bp = Blueprint('usuarios', __name__)

# --- 1. OBTENER TODOS (GET) ---
@datos_personales_bp.route('/usuarios', methods=['GET'])
def obtener_datos_demograficos():
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
    
# obterner usuario por id

@datos_personales_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM usuarios WHERE id = %s', (id,))
    resultado = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(resultado)


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
 


# --- 2. CREAR DATOS DEMOGRÁFICOS (POST) ---
@datos_personales_bp.route('/usuarios', methods=['POST'])
def crear_datos_personales():
    datos = request.json
    nombre = datos.get('nombre')
    apellido = datos.get('apellido')
    cedula = datos.get('cedula')
    contrasena = cedula  # Por defecto, la contraseña es la cédula 
    telefono = datos.get('telefono') 
    direccion = datos.get('direccion')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
        
    # SQL Actualizado con los nuevos campos
    sql = """
        INSERT INTO usuarios 
            (nombre, apellido, cedula, contrasena, telefono, direccion) 
            VALUES (%s, %s, %s, %s, %s, %s) 
            RETURNING *
        """
        
    cur.execute(sql, (nombre, apellido, cedula, contrasena, telefono, direccion))
        
    nuevo_usuario = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
        
    return jsonify(nuevo_usuario), 201
        


# --- 3. ACTUALIZAR DATOS DEMOGRÁFICOS (PUT) ---
@datos_personales_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_datos_demograficos(id):
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

# --- 4. ELIMINAR DATOS DEMOGRÁFICOS (DELETE) ---
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