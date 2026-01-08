--Este script SQL obtiene todos los datos relacionados con un usuario específico, incluyendo sus datos demográficos, domicilio, servicios básicos y datos académicos. 
SELECT 
    u.*, 
    dg.nacionalidad, dg.fecha_nacimiento, dg.estado_civil, dg.sexo, dg.autoidentificacion, dg.discapacidad, dg.pais, dg.provincia, dg.ciudad,
    d.barrio, d.calle_principal, d.calle_secundaria, d.numero_domicilio, d.tipo_vivienda,
    sb.agua_potable, sb.energia_electrica, sb.alcantarillado, sb.recoleccion_basura, sb.internet,
    da.titulo_homologado, da.unidad_educativa, da.tipo_unidad_educativa, da.calificacion, da.cuadro_honor, da.titulo_tercer_nivel, da.titulo_cuarto_nivel, da.fecha_registro_nacional
FROM usuarios u
LEFT JOIN datos_demograficos dg ON u.id = dg.usuario_id
LEFT JOIN domicilio d ON u.id = d.usuario_id
LEFT JOIN servicios_basicos sb ON u.id = sb.usuario_id
LEFT JOIN datos_academicos da ON u.id = da.usuario_id
WHERE u.id = 13;