
"""
Script para cargar un modelo de clasificación fine-tuned y hacer inferencias
desde texto plano. Requiere el mismo tokenizer/modelo usados en entrenamiento.
"""

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

# Ruta del modelo entrenado
MODEL_DIR = "./modelo_emocional"

# Cargar modelo y tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)

# Crear pipeline
clf_pipeline = pipeline("text-classification", model=model, tokenizer=tokenizer, top_k=1)

def predecir_emocion(texto):
    """Devuelve la emoción o diagnóstico más probable del texto dado."""
    resultado = clf_pipeline(texto[:512])[0]  # evitar textos muy largos
    return {"label": resultado["label"], "score": resultado["score"]}

# Ejemplo de uso
if __name__ == "__main__":
    texto = "Siento que no tengo energía ni ganas de hacer nada."
    prediccion = predecir_emocion(texto)
    print("Predicción:", prediccion)
