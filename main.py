"""
Archivo principal que inicia la aplicación Flask.
"""


# Importación de librerías
from flask import Flask
# Importación de librerías
from app.routes import register_routes

# Función: create_app
def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
