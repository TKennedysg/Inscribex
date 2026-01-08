from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor

servicios_bp = Blueprint('servicios_basicos', __name__)

@servicios_bp.route('/servicios-basicos', methods=['GET'])
def obtener_servicios():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM servicios_basicos')
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(resultado)

@servicios_bp.route('/servicios-basicos', methods=['POST'])
def crear_servicios():
    datos = request.json
    usuario_id = datos.get('usuario_id')

    if usuario_id is None:
        return jsonify({"mensaje": "usuario_id es obligatorio"}), 400

    agua_potable = datos.get('agua_potable')
    energia_electrica = datos.get('energia_electrica')
    alcantarillado = datos.get('alcantarillado')
    recoleccion_basura = datos.get('recoleccion_basura')
    internet = datos.get('internet')
    dispositivos_tecnologicos = datos.get('dispositivos_tecnologicos')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute(
        '''
        INSERT INTO servicios_basicos (
            usuario_id,
            agua_potable,
            energia_electrica,
            alcantarillado,
            recoleccion_basura,
            internet,
            dispositivos_tecnologicos
        ) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *
        ''',
        (
            usuario_id,
            agua_potable,
            energia_electrica,
            alcantarillado,
            recoleccion_basura,
            internet,
            dispositivos_tecnologicos
        )
    )
    
    nuevo_servicio = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify(nuevo_servicio), 201

@servicios_bp.route('/servicios-basicos/<int:id>', methods=['PUT'])
def actualizar_servicios(id):
    datos = request.json
    agua_potable = datos.get('agua_potable')
    energia_electrica = datos.get('energia_electrica')
    alcantarillado = datos.get('alcantarillado')
    recoleccion_basura = datos.get('recoleccion_basura')
    internet = datos.get('internet')
    dispositivos_tecnologicos = datos.get('dispositivos_tecnologicos')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute(
        '''
        UPDATE servicios_basicos 
        SET agua_potable = %s,
            energia_electrica = %s,
            alcantarillado = %s,
            recoleccion_basura = %s,
            internet = %s,
            dispositivos_tecnologicos = %s
        WHERE id = %s 
        RETURNING *
        ''',
        (
            agua_potable,
            energia_electrica,
            alcantarillado,
            recoleccion_basura,
            internet,
            dispositivos_tecnologicos,
            id
        )
    )
    
    servicio_actualizado = cur.fetchone()
    
    if servicio_actualizado is None:
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Registro no encontrado"}), 404

    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify(servicio_actualizado)

@servicios_bp.route('/servicios-basicos/<int:id>', methods=['DELETE'])
def eliminar_servicios(id):
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute('DELETE FROM servicios_basicos WHERE id = %s RETURNING *', (id,))
    servicio_eliminado = cur.fetchone()
    
    if servicio_eliminado is None:
        cur.close()
        conn.close()
        return jsonify({"mensaje": "Registro no encontrado"}), 404

    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"mensaje": f"Registro con ID {id} eliminado correctamente"}), 200
