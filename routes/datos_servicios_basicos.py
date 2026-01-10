from flask import Blueprint, request, jsonify
from dbconexion import get_db_connection
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import jwt_required, get_jwt_identity

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
            internet
        ) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *
        ''',
        (
            usuario_id,
            agua_potable,
            energia_electrica,
            alcantarillado,
            recoleccion_basura,
            internet,
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
        WHERE id = %s 
        RETURNING *
        ''',
        (
            agua_potable,
            energia_electrica,
            alcantarillado,
            recoleccion_basura,
            internet,
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



# ACTUALIZAR MI PERFIL (PUT) 

@servicios_bp.route('/servicios-basicos/actualizar', methods=['PUT'])
@jwt_required()
def actualizar_servicios_basicos():
    # 1. Extraemos el ID directamente del TOKEN (Seguridad total)
    usuario_id = get_jwt_identity()
    
    datos = request.json
    if not datos:
        return jsonify({"mensaje": "No hay datos para actualizar"}), 400

    # Campos que el propio usuario tiene permiso de cambiar
    campos_permitidos = ['agua_potable', 'energia_electrica', 'alcantarillado', 'recoleccion_basura', 'internet']
    partes_sql = []
    valores = []

    for campo in campos_permitidos:
        if campo in datos:
            partes_sql.append(f"{campo} = %s")
            valores.append(datos[campo])

    if not partes_sql:
        return jsonify({"mensaje": "Nada que actualizar"}), 400

    valores.append(usuario_id) # El ID viene del token, no de la URL

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    try:
        query = f"UPDATE servicios_basicos SET {', '.join(partes_sql)} WHERE id = %s RETURNING id, agua_potable, energia_electrica, alcantarillado, recoleccion_basura, internet"
        cur.execute(query, tuple(valores))
        servicios_basicos_actualizado = cur.fetchone()
        conn.commit()
        
        return jsonify({
            "mensaje": "Servicios básicos actualizados",
            "servicios_basicos": servicios_basicos_actualizado
        })
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
        conn.close()


# obtener informacion mediante jwtoken
@servicios_bp.route('/servicios-basicos', methods=['GET'])
@jwt_required()
def obtener_servicios_basicos():
    try:
        # Extrae el ID que guardamos en el login (identity)
        usuario_id = get_jwt_identity() 
        
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Aprovechamos para traer sus datos académicos con un JOIN
        cur.execute('SELECT * FROM servicios_basicos WHERE id = %s', (usuario_id,))
        
        servicios_basicos = cur.fetchone()
        
        cur.close()
        conn.close()

        if servicios_basicos:
            servicios_basicos.pop('usuario_id', None)
            return jsonify(servicios_basicos), 200
        else:
            return jsonify({"mensaje": "Servicios básicos no encontrados"}), 404

    except Exception as e:
        print(f"Error en perfil: {e}")
        return jsonify({"error": str(e)}), 500
 
