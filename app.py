from flask import Flask
from flask_cors import CORS
from routes.datos_personales import datos_personales_bp 
from routes.usuarios import usuarios_bp
<<<<<<< HEAD
from routes.datos_vivienda import vivienda_bp
=======
from routes.datos_academicos import datos_academicos_bp
from routes.datos_servicios_basicos import servicios_bp
>>>>>>> 8723c84c8f477c80b9727aba26883ca25716649c

app = Flask(__name__)
CORS(app)

app.register_blueprint(datos_personales_bp, url_prefix="/api/python")
app.register_blueprint(usuarios_bp, url_prefix="/api/python")
<<<<<<< HEAD
app.register_blueprint(vivienda_bp, url_prefix="/api/python")
=======
app.register_blueprint(datos_academicos_bp, url_prefix="/api/python")
app.register_blueprint(servicios_bp, url_prefix="/api/python")
>>>>>>> 8723c84c8f477c80b9727aba26883ca25716649c

if __name__ == "__main__":
    app.run(debug=True, port=4000)