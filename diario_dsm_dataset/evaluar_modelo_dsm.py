
"""
Evalúa el modelo DSM entrenado usando métricas de clasificación:
- Precisión
- Recall
- F1-score
Requiere:
- modelo_dsm/ con el modelo entrenado
- daicwoz_textos.csv con texto y label
"""

import pandas as pd
from sklearn.metrics import classification_report
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Rutas
MODEL_PATH = "./modelo_dsm"
DATA_PATH = "./daicwoz_textos.csv"

# Cargar modelo
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
clf = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Cargar dataset
df = pd.read_csv(DATA_PATH)
texts = df["texto"].tolist()
true_labels = df["label"].tolist()

# Predicción
pred_labels = []
for text in texts:
    result = clf(text[:512])[0]
    pred = 1 if result["label"] == "LABEL_1" else 0
    pred_labels.append(pred)

# Mostrar métricas
print("📊 Evaluación del Modelo DSM:")
print(classification_report(true_labels, pred_labels, digits=3, target_names=["No depresivo", "Depresión"]))
