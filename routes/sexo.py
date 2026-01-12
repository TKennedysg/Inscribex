from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import jwt_required, get_jwt_identity

sexo_bp = Blueprint('sexo', __name__)

#OBTENER SEXO (GET)
@sexo_bp.route('/obtener/sexo', methods=['GET'])
def obtener_sexo():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM sexo ORDER BY id ASC') # Agregué orden
        resultado = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
