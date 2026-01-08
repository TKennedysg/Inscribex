from flask import Flask
from flask_cors import CORS
from routes.datos_personales import datos_personales_bp 
#from routes.usuarios import usuarios_bp
from routes.datos_vivienda import vivienda_bp
from routes.datos_academicos import datos_academicos_bp
from routes.datos_servicios_basicos import servicios_bp
from routes.datos_periodo import periodos_bp
from routes.datos_carrera import datos_carreras_bp
from routes.datos_duracion_carrera import duracion_carreras_bp
from routes.datos_modalidad import modalidad_bp
from routes.datos_sede import sedes_bp
from routes.datos_area import areas_bp
from routes.datos_notas_postulacion import notas_postulacion_bp
from routes.datos_jornadas_academicas import jornadas_academicas_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(datos_personales_bp, url_prefix="/api/python")
#app.register_blueprint(usuarios_bp, url_prefix="/api/python")
app.register_blueprint(vivienda_bp, url_prefix="/api/python")
app.register_blueprint(datos_academicos_bp, url_prefix="/api/python")
app.register_blueprint(servicios_bp, url_prefix="/api/python")
app.register_blueprint(datos_carreras_bp, url_prefix="/api/python")
app.register_blueprint(duracion_carreras_bp, url_prefix="/api/python")
app.register_blueprint(modalidad_bp, url_prefix="/api/python")
app.register_blueprint(periodos_bp, url_prefix="/api/python")
app.register_blueprint(sedes_bp, url_prefix="/api/python")
app.register_blueprint(areas_bp, url_prefix="/api/python")
app.register_blueprint(notas_postulacion_bp, url_prefix="/api/python")
app.register_blueprint(jornadas_academicas_bp, url_prefix="/api/python")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)