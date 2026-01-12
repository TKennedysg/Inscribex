from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

facultad_bp = Blueprint('facultades', __name__)

# --- 1. OBTENER TODOS (GET) ---
@facultad_bp.route('/obtener/facultades', methods=['GET'])
def obtener_facultad():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM facultad ORDER BY id ASC') 
        resultado = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}), 500