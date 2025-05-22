
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "supersecreto123"  # En producción, usar variable de entorno
ALGORITHM = "HS256"
EXPIRACION_MINUTOS = 60

def crear_token(usuario):
    payload = {
        "sub": usuario,
        "exp": datetime.utcnow() + timedelta(minutes=EXPIRACION_MINUTOS)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
