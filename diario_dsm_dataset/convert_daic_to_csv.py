
"""
Versión final del convertidor DAIC-WOZ que:
- Usa separador por tabulación para leer correctamente los .csv
- Verifica que existan columnas 'speaker' y 'value'
- Loguea participantes con texto válido o ignorados
"""

import os
import pandas as pd

# Rutas
TRANSCRIPTS_DIR = "./transcripts"
PHQ8_CSV = "./PHQ8_Scores.csv"
OUTPUT_CSV = "./daicwoz_textos.csv"
MIN_PALABRAS = 3

def cargar_phq_labels(csv_path):
    df = pd.read_csv(csv_path)
    df = df[["Participant_ID", "PHQ_Binary"]]
    df = df.rename(columns={"PHQ_Binary": "label"})
    return dict(zip(df["Participant_ID"], df["label"]))

def cargar_transcripciones(dir_path):
    textos = {}
    for fname in os.listdir(dir_path):
        if fname.endswith(".csv") and "TRANSCRIPT" in fname:
            pid = int(''.join(filter(str.isdigit, fname)))
            try:
                df = pd.read_csv(os.path.join(dir_path, fname), sep='\t')
                if "speaker" in df.columns and "value" in df.columns:
                    participant_lines = df[df["speaker"].str.lower() == "participant"]
                    texto = " ".join(participant_lines["value"].dropna().astype(str).tolist()).strip()
                    n_palabras = len(texto.split())
                    if n_palabras >= MIN_PALABRAS:
                        textos[pid] = texto
                        print(f"✅ {pid}: {n_palabras} palabras incluidas.")
                    else:
                        print(f"⚠️ {pid}: solo {n_palabras} palabras del participante. Ignorado.")
                else:
                    print(f"❌ {pid}: columnas 'speaker' o 'value' no encontradas.")
            except Exception as e:
                print(f"❌ {pid}: error al leer el archivo - {e}")
    return textos

def generar_csv(textos, etiquetas, output_csv):
    rows = []
    for pid, texto in textos.items():
        if pid in etiquetas:
            rows.append({
                "texto": texto,
                "label": etiquetas[pid]
            })
        else:
            print(f"❗ {pid} no tiene etiqueta PHQ, se ignora.")
    df = pd.DataFrame(rows)
    df.to_csv(output_csv, index=False)
    print(f"✅ Archivo generado: {output_csv} con {len(df)} muestras.")

if __name__ == "__main__":
    labels = cargar_phq_labels(PHQ8_CSV)
    textos = cargar_transcripciones(TRANSCRIPTS_DIR)
    generar_csv(textos, labels, OUTPUT_CSV)
