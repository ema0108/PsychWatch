
# 🧠 Diario Psicológico IA — Documentación Técnica Profesional

Este proyecto es un backend modular para registro emocional, análisis automático y diagnóstico clínico preliminar usando inteligencia artificial. Fue diseñado para integrarse en entornos clínicos o de autoayuda con trazabilidad psicológica.

Incluye:
- 📌 Autenticación con JWT
- 📋 Registro de entradas en SQLite
- 📊 Análisis emocional (sentimiento + emociones)
- 🧠 Diagnóstico basado en reglas DSM-5
- 🤖 Clasificador DSM con IA entrenado en DAIC-WOZ
- 🔍 Estadísticas longitudinales
- 🧪 Sistema de entrenamiento + evaluación con `transformers`
- ⚙️ Dockerfile y despliegue en Render

## Flujo de trabajo

1. Usuario envía entrada → `/guardar`
2. Análisis con:
   - `TextBlob` / `Transformers`
   - Emociones con modelo fine-tuned o reglas
   - DSM heurístico + modelo DSM si está disponible
3. Entrada guardada y recuperable por `/historial` y `/estadisticas`

## Módulos clave

- `analysis_service.py`: orquesta todo
- `sentiment.py`, `emotions.py`, `diagnostics.py`: subanálisis
- `db.py`: persistencia
- `routes.py`, `auth.py`: endpoints y login
- `train_dsm_classifier.py` + `predict_dsm.py`: IA clínica personalizada

¡Listo para producción, investigación o integración con frontend React!
