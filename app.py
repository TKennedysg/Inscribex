from flask import Flask
from flask_cors import CORS
from routes.datos_personales import datos_personales_bp 

app = Flask(__name__)
CORS(app)

app.register_blueprint(datos_personales_bp, url_prefix="/api/python")

if __name__ == "__main__":
    app.run(debug=True, port=4000)