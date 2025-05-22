"""
Acceso a la base de datos SQLite: guardar y recuperar entradas del diario.
"""


# Importación de librerías
import sqlite3
# Importación de librerías
import json
# Importación de librerías
from datetime import datetime

DB_PATH = "journal.sqlite3"

# Función: conectar
def conectar():
    return sqlite3.connect(DB_PATH)

# Función: crear_tabla
def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entradas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            texto TEXT NOT NULL,
            sentimiento TEXT,
            emociones TEXT,
            diagnostico TEXT,
            fecha TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Función: guardar_entrada
def guardar_entrada(usuario, texto, sentimiento, emociones, diagnostico):
    crear_tabla()  # Asegura que la tabla exista

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO entradas (usuario, texto, sentimiento, emociones, diagnostico, fecha) VALUES (?, ?, ?, ?, ?, ?)",
        (
            usuario,
            texto,
            json.dumps(sentimiento, ensure_ascii=False),
            json.dumps(emociones, ensure_ascii=False),
            json.dumps(diagnostico, ensure_ascii=False),
            datetime.now().isoformat()
        )
    )
    conn.commit()
    conn.close()

# Función: obtener_historial
def obtener_historial(usuario):
    crear_tabla()

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, texto, sentimiento, emociones, diagnostico, fecha FROM entradas WHERE usuario = ? ORDER BY fecha DESC", (usuario,))
    rows = cursor.fetchall()
    conn.close()

    historial = []
    for row in rows:
        historial.append({
            "id": row[0],
            "texto": row[1],
            "sentimiento": json.loads(row[2]),
            "emociones": json.loads(row[3]),
            "diagnostico": json.loads(row[4]),
            "fecha": row[5]
        })
    return historial
