from flask import Flask
from flask_cors import CORS
from routes.usuarios import usuarios_bp
from routes.datos_academicos import datos_academicos_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(usuarios_bp, url_prefix="/api/python")
app.register_blueprint(datos_academicos_bp, url_prefix="/api/python")

if __name__ == "__main__":
    app.run(debug=True, port=4000)