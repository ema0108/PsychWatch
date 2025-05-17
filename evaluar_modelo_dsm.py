
"""
Evalúa el modelo DSM entrenado usando métricas clásicas:
- Precisión
- Recall (sensibilidad)
- F1-score

Este script requiere que:
1. El modelo esté entrenado en ./modelo_dsm/
2. Se tenga un archivo daicwoz_textos.csv con 'texto' y 'label'
"""

import pandas as pd
from sklearn.metrics import classification_report
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Ruta del modelo y datos
MODEL_PATH = "./modelo_dsm"
DATA_PATH = "./daicwoz_textos.csv"

# Cargar modelo
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
clf = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Cargar datos
df = pd.read_csv(DATA_PATH)
texts = df["texto"].tolist()
true_labels = df["label"].tolist()

# Predecir etiquetas
pred_labels = []
for text in texts:
    res = clf(text[:512])[0]
    pred = 1 if res["label"] == "LABEL_1" else 0
    pred_labels.append(pred)

# Reporte de métricas
print("🧪 Evaluación del modelo DSM:
")
print(classification_report(true_labels, pred_labels, digits=3, target_names=["No Depresivo", "Depresión"]))
