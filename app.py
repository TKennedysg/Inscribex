from flask import Flask
from flask_cors import CORS
from routes.datos_personales import datos_personales_bp 
from routes.modalidad import modalidad_bp
from routes.datos_vivienda import vivienda_bp
from routes.datos_academicos import datos_academicos_bp
from routes.datos_servicios_basicos import servicios_bp
from routes.datos_periodo import periodos_bp
from routes.datos_sede import sedes_bp
from routes.datos_area import areas_bp
from routes.datos_notas_postulacion import notas_postulacion_bp
from routes.datos_demograficos import datos_demograficos_bp
from routes.datos_postulacion import postulacion_bp
from routes.datos_verificacion_registro_nacional import verificacion_bp
<<<<<<< HEAD
from routes.oferta_academica import oferta_academica_bp
from routes.datos_carrera import datos_carreras_bp
from routes.datos_jornadas_academicas import jornadas_academicas_bp
from routes.tipo_cupo import tipo_cupo_bp
from routes.inscripcion import inscripcion_bp
from routes.nacionalidad import nacionalidad_bp
from routes.provincia import provincia_bp
from routes.estado_civil import estado_civil_bp
from routes.sexo import sexo_bp
from routes.autoidentificacion import autoidentificacion_bp
from routes.ciudad import ciudad_bp
from routes.pais import pais_bp

=======
from routes.inscripcion import inscripcion_bp
>>>>>>> 3f51995a21a6ae940aba8f16aacfdf6357971860
from routes.login import login_bp
from init_db import Usuario
import os
from flask_jwt_extended import JWTManager



app = Flask(__name__, static_url_path='/static', static_folder='static')
CORS(app)

# agregamos configuracion para JWT
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'clave-secreta-de-respaldo')
jwt = JWTManager(app)

app.register_blueprint(datos_personales_bp, url_prefix="/api/python")
app.register_blueprint(vivienda_bp, url_prefix="/api/python")
app.register_blueprint(datos_academicos_bp, url_prefix="/api/python")
app.register_blueprint(servicios_bp, url_prefix="/api/python")
app.register_blueprint(periodos_bp, url_prefix="/api/python")
app.register_blueprint(sedes_bp, url_prefix="/api/python")
app.register_blueprint(areas_bp, url_prefix="/api/python")
app.register_blueprint(notas_postulacion_bp, url_prefix="/api/python")
app.register_blueprint(datos_demograficos_bp, url_prefix="/api/python")
app.register_blueprint(login_bp, url_prefix="/api/python")
app.register_blueprint(verificacion_bp, url_prefix="/api/python")
app.register_blueprint(postulacion_bp, url_prefix="/api/python")    
<<<<<<< HEAD
app.register_blueprint(modalidad_bp, url_prefix="/api/python")    
app.register_blueprint(oferta_academica_bp, url_prefix="/api/python")   
app.register_blueprint(datos_carreras_bp, url_prefix="/api/python")
app.register_blueprint(jornadas_academicas_bp, url_prefix="/api/python")
app.register_blueprint(tipo_cupo_bp, url_prefix="/api/python")  
app.register_blueprint(inscripcion_bp, url_prefix="/api/python")
app.register_blueprint(nacionalidad_bp, url_prefix="/api/python")
app.register_blueprint(provincia_bp, url_prefix="/api/python")
app.register_blueprint(estado_civil_bp, url_prefix="/api/python")
app.register_blueprint(sexo_bp, url_prefix="/api/python")
app.register_blueprint(autoidentificacion_bp, url_prefix="/api/python")
app.register_blueprint(ciudad_bp, url_prefix="/api/python")
app.register_blueprint(pais_bp, url_prefix="/api/python")


=======
app.register_blueprint(inscripcion_bp, url_prefix="/api/python")
>>>>>>> 3f51995a21a6ae940aba8f16aacfdf6357971860

Usuario.crear_tablas()
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)