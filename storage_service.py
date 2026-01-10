import os
import uuid

# Carpeta donde se guardarán las fotos
UPLOAD_FOLDER = 'static/uploads'

# Crear la carpeta si no existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def guardar_imagen_local(archivo):
    try:
        # 1. Extraer la extensión de forma segura
        # Esto evita errores si el archivo no tiene punto
        nombre_original = archivo.filename
        if '.' in nombre_original:
            extension = nombre_original.rsplit('.', 1)[1].lower()
        else:
            extension = 'jpg' # Extensión por defecto si no tiene

        # 2. Generar nombre único con UUID
        nombre_unico = f"{uuid.uuid4()}.{extension}"
        
        # 3. Ruta completa donde se guardará (en el disco duro)
        ruta_guardado = os.path.join(UPLOAD_FOLDER, nombre_unico)
        
        # 4. Guardar físicamente el archivo
        archivo.save(ruta_guardado)
        
        # 5. Retornar la URL relativa (para la base de datos)
        # Limpiamos los espacios extras para que la URL sea perfecta
        return f"/static/uploads/{nombre_unico}"
        
    except Exception as e:
        print(f"Error guardando localmente: {e}")
        return None
 
