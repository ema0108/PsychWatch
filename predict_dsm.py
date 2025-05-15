
"""
Inferencia de texto con modelo DSM entrenado (clasificación depresión sí/no).
"""
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("./modelo_dsm")
model = AutoModelForSequenceClassification.from_pretrained("./modelo_dsm")
clf = pipeline("text-classification", model=model, tokenizer=tokenizer)

def detectar_depresion(texto):
    res = clf(texto[:512])[0]
    return {
        "clasificacion": "Depresión" if res["label"] == "LABEL_1" else "No depresivo",
        "confianza": round(res["score"], 3)
    }

if __name__ == "__main__":
    print(detectar_depresion("Me siento sin energía y no tengo motivación desde hace semanas."))
