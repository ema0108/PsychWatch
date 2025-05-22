"""
Lógica de autenticación con JWT.
"""


# Importación de librerías
from flask import request, jsonify
# Importación de librerías
from core.security import crear_token

# Función: register_auth_routes
def register_auth_routes(app):

    @app.route("/login", methods=["POST"])
# Función: login
    def login():
        data = request.get_json()
        usuario = data.get("usuario")

        if not usuario:
            return jsonify({"error": "Falta el campo 'usuario'"}), 400

        token = crear_token(usuario)
        return jsonify({"token": token})
