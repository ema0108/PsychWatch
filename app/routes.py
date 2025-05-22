"""
Rutas principales del backend. Define los endpoints públicos y protegidos.
"""


# Importación de librerías
from functools import wraps
# Importación de librerías
from flask import request, jsonify
# Importación de librerías
from core.security import verificar_token
from services.analysis_service import procesar_entrada_completa


# Función: requiere_token
def requiere_token(f):
    @wraps(f)
# Función: wrapper
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization", "")
        if not auth.startswith("Bearer "):
            return jsonify({"error": "Token no proporcionado"}), 401
        token = auth.replace("Bearer ", "")
        usuario = verificar_token(token)
        if not usuario:
            return jsonify({"error": "Token inválido o expirado"}), 401
        request.usuario = usuario  # inyectamos usuario en request
        return f(*args, **kwargs)
    return wrapper


# Importación de librerías
from app.auth import register_auth_routes

# Importación de librerías
from flask import request, jsonify
# Importación de librerías
from services.analysis_service import analizar_texto, guardar_entrada_servicio, obtener_historial_servicio

# Función: register_routes
def register_routes(app):

    @app.route("/")
# Función: home
    def home():
        return jsonify({"status": "ok", "message": "API modular funcionando"})

    @app.route("/analizar", methods=["POST"])
# Función: analizar
    def analizar():
        data = request.get_json()
        texto = data.get("texto", "")
        resultado = analizar_texto(texto)
        return jsonify(resultado)

    @app.route("/guardar", methods=["POST"])
# Función: guardar
    def guardar():
        data = request.get_json()
        usuario = data.get("usuario")
        texto = data.get("texto")
        if not usuario or not texto:
            return jsonify({"error": "Faltan campos requeridos"}), 400
        resultado = guardar_entrada_servicio(usuario, texto)
        return jsonify(resultado)

    @app.route("/historial/<usuario>", methods=["GET"])
# Función: historial
    def historial(usuario):
        historial = obtener_historial_servicio(usuario)
        return jsonify(historial)
    @app.route("/estadisticas/<usuario>", methods=["GET"])
# Función: estadisticas
    def estadisticas(usuario):
# Importación de librerías
        from services.stats_service import analizar_estadisticas
        resumen = analizar_estadisticas(usuario)
        return jsonify(resumen)
    register_auth_routes(app)


from flask import Blueprint, request, jsonify
from services.analysis_service import procesar_entrada_completa

routes = Blueprint("routes", __name__)
diagnosticos = {}

@routes.route("/guardar_entrada", methods=["POST"])
def guardar_entrada():
    data = request.get_json()
    texto = data.get("texto", "")
    usuario = data.get("usuario", "anonimo")

    resultado = procesar_entrada_completa(texto)
    diagnosticos[usuario] = resultado

    return jsonify(resultado)

@routes.route("/ultimos_diagnosticos", methods=["GET"])
def ultimos_diagnosticos():
    usuario = request.args.get("usuario", "paciente1")
    return jsonify(diagnosticos.get(usuario, {}))
