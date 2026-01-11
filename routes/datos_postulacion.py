# id usuario carrera id sede id area nota == 450 a 10000
from flask import Blueprint, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import jwt_required
import random

postulacion_bp = Blueprint('postulacion', __name__)

class Postulacion:
    def __init__(self, postulacion_id):
        self.postulacion_id = postulacion_id
        self.nota_examen = None

    def generar_nota_examen(self):
        self.nota_examen = random.randint(450, 1000)  # rango corregido
        return self.nota_examen

    def guardar_nota(self):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        sql = """
        UPDATE postulacion
        SET nota_examen = %s
        WHERE id = %s
        RETURNING *
        """

        cur.execute(sql, (self.nota_examen, self.postulacion_id))
        resultado = cur.fetchone()
        conn.commit()

        cur.close()
        conn.close()

        return resultado


@postulacion_bp.route('/postulacion/<int:id>/generar-nota', methods=['POST'])
@jwt_required()  # solo admin
def generar_nota_postulacion(id):
    try:
        postulacion = Postulacion(id)
        nota = postulacion.generar_nota_examen()
        resultado = postulacion.guardar_nota()

        if not resultado:
            return jsonify({"mensaje": "Postulación no encontrada"}), 404

        return jsonify({
            "mensaje": "Nota de examen generada correctamente",
            "nota_examen": nota,
            "postulacion": resultado
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
