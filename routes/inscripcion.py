from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import jwt_required, get_jwt_identity

inscripcion_bp = Blueprint('inscripcion', __name__)

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

