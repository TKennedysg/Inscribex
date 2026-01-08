from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

sedes_bp = Blueprint('sedes', __name__)

# --- OBTENER TODAS LAS SEDES (GET) ---
@sedes_bp.route('/sedes', methods=['GET'])
def obtener_sedes():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute('SELECT * FROM sedes')
    resultado = cur.fetchall()
    
    cur.close()
    conn.close()
    return jsonify(resultado)


# --- CREAR UNA NUEVA SEDE (POST) ---
@sedes_bp.route('/sedes', methods=['POST'])
def crear_sede():
    datos = request.json
    nombre_sede = datos.get('nombre_sede')
    direccion = datos.get('direccion')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        '''
        INSERT INTO sedes (nombre_sede, direccion)
        VALUES (%s, %s)
        RETURNING *
        ''',
        (nombre_sede, direccion)
    )

    nueva_sede = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(nueva_sede), 201


# --- ACTUALIZAR UNA SEDE (PUT) ---
@sedes_bp.route('/sedes/<int:id>', methods=['PUT'])
def actualizar_sede(id):
    datos = request.json
    nombre_sede = datos.get('nombre_sede')
    direccion = datos.get('direccion')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(
        '''
        UPDATE sedes
        SET nombre_sede = %s, direccion = %s
        WHERE id = %s
        RETURNING *
        ''',
        (nombre_sede, direccion, id)
    )

    sede_actualizada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    # Manejo básico de error si no existe el ID
    if sede_actualizada is None:
        return jsonify({'mensaje': 'Sede no encontrada'}), 404

    return jsonify(sede_actualizada)


# --- ELIMINAR UNA SEDE (DELETE) ---
@sedes_bp.route('/sedes/<int:id>', methods=['DELETE'])
def eliminar_sede(id):
    conn = get_db_connection()
    cur = conn.cursor() # Aquí no es estrictamente necesario RealDictCursor si solo borras, pero funciona igual

    cur.execute(
        'DELETE FROM sedes WHERE id = %s RETURNING *',
        (id,)
    )

    sede_eliminada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if sede_eliminada is None:
        return jsonify({'mensaje': 'Sede no encontrada'}), 404

    return jsonify({'mensaje': 'Sede eliminada correctamente', 'registro': sede_eliminada}), 200