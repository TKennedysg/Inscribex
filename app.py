from flask import Flask
from flask_cors import CORS
<<<<<<< HEAD
from routes.datos_personales import datos_personales_bp 
=======
from routes.usuarios import usuarios_bp
from routes.datos_academicos import datos_academicos_bp
from routes.datos_servicios_basicos import servicios_bp
>>>>>>> 1c1ffb9b6d232a96a4857c1dcf3512aa04586b6f

app = Flask(__name__)
CORS(app)

<<<<<<< HEAD
app.register_blueprint(datos_personales_bp, url_prefix="/api/python")
=======
app.register_blueprint(usuarios_bp, url_prefix="/api/python")
app.register_blueprint(datos_academicos_bp, url_prefix="/api/python")
app.register_blueprint(servicios_bp, url_prefix="/api/python")
>>>>>>> 1c1ffb9b6d232a96a4857c1dcf3512aa04586b6f

if __name__ == "__main__":
    app.run(debug=True, port=4000)