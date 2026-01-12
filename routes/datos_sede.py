from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

sedes_bp = Blueprint('sedes', __name__)

# --- OBTENER TODAS LAS SEDES (GET) ---
@sedes_bp.route('/obtener/sedes', methods=['GET'])
def obtener_sedes():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute('SELECT * FROM sedes')
    resultado = cur.fetchall()
    
    cur.close()
    conn.close()
    return jsonify(resultado)

