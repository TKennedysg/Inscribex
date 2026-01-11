from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

login_bp = Blueprint('login', __name__)
@login_bp.route('/login', methods=['POST'])
def login():
    datos = request.json
    cedula = datos.get('cedula')
    contrasena = datos.get('contrasena')

    # 1. Buscar el usuario en la DB
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM usuarios WHERE cedula = %s", (cedula,))
    usuario = cur.fetchone()
    cur.close()
    conn.close()

    # 2. Verificar credenciales (Aquí comparamos texto plano por ahora)
    if usuario and usuario['contrasena'] == contrasena:
        # 3. Crear el token JWT
        # Guardamos el ID del usuario dentro del token
        access_token = create_access_token(identity=str(usuario['id']))
        
        return jsonify({
            "mensaje": "Login exitoso",
            "token": access_token,
            "usuario": {
                "id": usuario['id'],
                "nombre": usuario['nombre'],
                "apellido": usuario['apellido'],
                "rol": usuario['rol']
            }
        }), 200
    
    return jsonify({"mensaje": "Cédula o contraseña incorrectos"}), 401
