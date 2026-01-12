from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import jwt_required, get_jwt_identity

estado_civil_bp = Blueprint('estado_civil', __name__)

#OBTENER ESTADO CIVIL (GET)
@estado_civil_bp.route('/obtener/estado-civil', methods=['GET'])
def obtener_estado_civil():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM estado_civil ORDER BY id ASC') # Agregué orden
        resultado = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
