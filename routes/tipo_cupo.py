from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

tipo_cupo_bp = Blueprint('tipos-cupos', __name__)

# --- 1. OBTENER TODOS (GET) ---
@tipo_cupo_bp.route('/obtener/tipo-cupo', methods=['GET'])
def obtener_tipo_cupo():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM tipo_cupo ORDER BY id ASC') 
        resultado = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

