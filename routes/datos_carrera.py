from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

datos_carreras_bp = Blueprint('datos_carreras', __name__)

# --- 1. OBTENER TODOS (GET) ---
@datos_carreras_bp.route('/obtener/carreras', methods=['GET'])
def obtener_datos_carreras():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM carreras ORDER BY id ASC') # Agregué orden
        resultado = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#OBTENER UNA CARRERA POR ID
@datos_carreras_bp.route('/datos-carreras/<int:id>', methods=['GET'])
def obtener_datos_carrera_por_id(id):
    conn = get_db_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("""
            SELECT 
                c.id,
                c.nombre_carrera,
                f.nombre_facultad,
                d.nombre_duracion
            FROM carreras c
            JOIN facultades f ON c.id_facultad = f.id
            JOIN duracion_carreras d ON c.id_duracion_carrera = d.id
            WHERE c.id = %s
        """, (id,))

        carrera = cursor.fetchone()

        if carrera:
            print("\nDETALLE DE LA CARRERA:")
            print(f"ID: {carrera[0]}")
            print(f"Carrera: {carrera[1]}")
            print(f"Facultad: {carrera[2]}")
            print(f"Duración: {carrera[3]}")
        else:
            print("❌ No se encontró una carrera con ese ID")

    except Exception as e:
        print("Error al obtener la carrera:", e)

    finally:
        cursor.close()
        conn.close()

    return jsonify(carrera)




@datos_carreras_bp.route('/datos-carreras', methods=['POST'])
def crear_datos_carreras():
    datos = request.json
    usuario_id = datos.get('usuario_id')
    id_modalidad = datos.get('id_modalidad')
    id_duracion_carrera = datos.get('id_duracion_carrera')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        '''
        INSERT INTO datos_carreras (
            usuario_id,
            id_modalidad,
            id_duracion_carrera
        ) VALUES (%s, %s, %s)
        RETURNING *
        ''',
        (
            usuario_id,
            id_modalidad,
            id_duracion_carrera
        )
    )

    nuevo_registro = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(nuevo_registro), 201


@datos_carreras_bp.route('/datos-carreras/<int:id>', methods=['PUT'])
def actualizar_datos_carreras(id):
    datos = request.json
    id_modalidad = datos.get('id_modalidad')
    id_duracion_carrera = datos.get('id_duracion_carrera')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        '''
        UPDATE datos_carreras
        SET id_modalidad = %s,
            id_duracion_carrera = %s
        WHERE id = %s
        RETURNING *
        ''',
        (
            id_modalidad,
            id_duracion_carrera,
            id
        )
    )

    registro_actualizado = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(registro_actualizado)


@datos_carreras_bp.route('/datos-carreras/<int:id>', methods=['DELETE'])
def eliminar_datos_carreras(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        'DELETE FROM datos_carreras WHERE id = %s RETURNING *',
        (id,)
    )

    registro_eliminado = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(registro_eliminado), 200
