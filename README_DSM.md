
# 📘 Diario Psicológico IA — Entrenamiento con DAIC-WOZ

Este documento explica paso a paso cómo usar el dataset **DAIC-WOZ** (Distress Analysis Interview Corpus) para entrenar un modelo de inteligencia artificial que detecte automáticamente posibles casos de **depresión** en entradas escritas por usuarios.

## ✅ ¿Qué es DAIC-WOZ?

Es un conjunto de datos creado por psicólogos y científicos que contiene:
- Transcripciones de entrevistas clínicas reales (en texto)
- Puntuaciones profesionales (PHQ-8) que indican nivel de depresión

Este dataset está diseñado específicamente para entrenar modelos clínicos automáticos.

---

## 🛠 Archivos necesarios

1. **transcripts/** → Carpeta con entrevistas en texto (.txt)
2. **PHQ8_Scores.csv** → Tabla con puntuaciones clínicas de cada participante
3. `convert_daic_to_csv.py` → Script que convierte los archivos anteriores a un CSV unificado
4. `train_dsm_classifier.py` → Entrena el modelo DSM con IA
5. `predict_dsm.py` → Usa el modelo para hacer predicciones desde texto

---

## 1️⃣ Paso 1: Preparar los archivos

Debes tener en tu carpeta estos elementos:

```
📂 transcripts/
    ├── TRANSCRIPT_P300.txt
    ├── TRANSCRIPT_P301.txt
    └── ...
📄 PHQ8_Scores.csv
📄 convert_daic_to_csv.py
```

---

## 2️⃣ Paso 2: Crear el archivo de entrenamiento

Corre este comando en tu terminal:

```bash
python convert_daic_to_csv.py
```

Este script va a:

- Leer cada entrevista
- Asociar su texto con la puntuación del paciente
- Generar un nuevo archivo llamado: `daicwoz_textos.csv`

Este archivo tendrá 2 columnas:
| texto (contenido de la entrevista) | label (0 o 1) |
|------------------------------------|---------------|
| "No me siento bien desde hace días"| 1             |
| "Estoy bien, gracias"              | 0             |

---

## 3️⃣ Paso 3: Entrenar el modelo DSM

Ahora ejecuta:

```bash
python train_dsm_classifier.py
```

Este programa va a:

- Leer el archivo `daicwoz_textos.csv`
- Dividirlo en entrenamiento y prueba
- Usar inteligencia artificial (modelo BERT) para aprender patrones reales de depresión
- Guardar el modelo listo para usarse en `./modelo_dsm/`

---

## 4️⃣ Paso 4: Usar el modelo en tu backend

El backend ya está preparado para detectar automáticamente si el modelo DSM está disponible.

Al usar el endpoint `/analizar` o `/guardar`, se incluirá esta sección:

```json
"dsm_clasificacion": {
  "clasificacion_dsm": "Depresión",
  "confianza": 0.91
}
```

---

## 5️⃣ Paso 5: Hacer pruebas manuales

También puedes probar el modelo directamente con:

```bash
python predict_dsm.py
```

Y escribiendo frases como:

```text
No tengo ganas de hacer nada desde hace semanas.
```

El programa responderá con una predicción y nivel de confianza.

---

## 📌 Resumen

Este sistema combina:
- Ciencia psicológica (PHQ-8 y DAIC-WOZ)
- Tecnología avanzada (BERT y Transformers)
- Explicaciones claras para que cualquier persona pueda usarlo

Está diseñado tanto para profesionales como para desarrolladores que quieran incorporar diagnóstico emocional en sus aplicaciones.

