from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

modalidad_bp = Blueprint('modalidades', __name__)

# --- 1. OBTENER TODOS (GET) ---
@modalidad_bp.route('/obtener/modalidades', methods=['GET'])
def obtener_modalidad():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM modalidad ORDER BY id ASC') 
        resultado = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}), 500