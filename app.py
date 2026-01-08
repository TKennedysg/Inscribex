from flask import Flask
from flask_cors import CORS
from routes.datos_personales import datos_personales_bp 
# from routes.usuarios import usuarios_bp
from routes.datos_vivienda import vivienda_bp
from routes.datos_academicos import datos_academicos_bp
from routes.datos_servicios_basicos import servicios_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(datos_personales_bp, url_prefix="/api/python")
# app.register_blueprint(usuarios_bp, url_prefix="/api/python")
app.register_blueprint(vivienda_bp, url_prefix="/api/python")
app.register_blueprint(datos_academicos_bp, url_prefix="/api/python")
app.register_blueprint(servicios_bp, url_prefix="/api/python")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)