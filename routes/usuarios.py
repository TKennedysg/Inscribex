from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM usuarios')
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(resultado)

@usuarios_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.json
    nombre = datos.get('nombre')
    apellido = datos.get('apellido')
    cedula = datos.get('cedula')
    contrasena = datos.get('contrasena') # Recuerda: ¡luego hay que encriptarla!

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute(
        'INSERT INTO usuarios (nombre, apellido, cedula, contrasena) VALUES (%s, %s, %s, %s) RETURNING *',
        (nombre, apellido, cedula, contrasena)
    )
    
    nuevo_usuario = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify(nuevo_usuario), 201

# --- 3. ACTUALIZAR USUARIO (PUT) ---
@usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    datos = request.json
    nombre = datos.get('nombre')
    apellido = datos.get('apellido')
    cedula = datos.get('cedula')
    # Nota: No solemos actualizar la contraseña en el mismo perfil por seguridad, 
    # pero si lo necesitas, puedes agregarla aquí.

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    # Ejecutamos el UPDATE
    # http://localhost:4000/api/python/usuarios/4
    cur.execute(
        """
        UPDATE usuarios 
        SET nombre = %s, apellido = %s, cedula = %s 
        WHERE id = %s 
        RETURNING *
        """,
        (nombre, apellido, cedula, id)
    )
    
    usuario_actualizado = cur.fetchone()
    
    if usuario_actualizado is None:
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify(usuario_actualizado)


# --- 4. ELIMINAR USUARIO (DELETE) ---
@usuarios_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Ejecutamos el DELETE
    cur.execute('DELETE FROM usuarios WHERE id = %s RETURNING *', (id,))
    usuario_eliminado = cur.fetchone()
    
    if usuario_eliminado is None:
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"mensaje": f"Usuario con ID {id} eliminado correctamente"}), 200