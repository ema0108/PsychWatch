
# 🧠 Diario Psicológico Backend (Modular)

Este proyecto es un backend completo para una aplicación de diario emocional inteligente.
Incluye análisis de texto, detección de emociones, diagnósticos preliminares, autenticación JWT, API REST y posibilidad de entrenar tu propio modelo de IA.

---

## 🚀 Endpoints principales

| Método | Ruta                       | Descripción                                  |
|--------|----------------------------|----------------------------------------------|
| POST   | `/login`                  | Autenticación por usuario (token JWT)        |
| POST   | `/guardar`                | Guarda entrada analizada (requiere token)    |
| GET    | `/historial/<usuario>`    | Muestra entradas guardadas (requiere token)  |
| GET    | `/estadisticas/<usuario>` | Analiza emociones y sentimiento históricos    |
| POST   | `/analizar`               | Análisis rápido sin guardar entrada          |

---

## 🛠 Requisitos

- Python 3.8+
- Flask, transformers, datasets, pandas, scikit-learn

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución

```bash
python main.py
```

---

## 🔐 Autenticación JWT

1. `POST /login` con JSON:
```json
{ "usuario": "juan123" }
```

2. Usa el token JWT en cada llamada protegida:

```
Authorization: Bearer <token>
```

---

## 📈 Estadísticas

El endpoint `/estadisticas/<usuario>` analiza todas las entradas para mostrar:

- Emociones más frecuentes
- Promedio de sentimiento
- Rango de fechas de uso

---

## 🧠 Entrenamiento de tu propia IA emocional

### 1. 🔍 Recolecta un dataset

Requiere un CSV con dos columnas:
| texto                              | label       |
|-----------------------------------|-------------|
| Me siento vacío desde hace días. | depresión   |
| Estoy muy feliz últimamente.     | alegría     |

Guarda como: `dataset_emociones.csv`

#### Datasets sugeridos:
- [GoEmotions (Google)](https://github.com/google-research/goemotions)
- [DAIC-WOZ (USC)](https://dcapswoz.ict.usc.edu/)
- [ISEAR](https://www.unige.ch/cisa/research/materials-and-online-research/research-material/)

---

### 2. 🧪 Entrenar el modelo

```bash
python fine_tune_emotions.py
```

Esto entrenará un modelo con Hugging Face Transformers y lo guardará en `./modelo_emocional/`.

---

### 3. 🤖 Usar el modelo

```bash
python predict_emotion.py
```

Esto cargará el modelo entrenado y hará inferencias desde texto.

---

### 4. 🔁 Integración automática

Cuando `./modelo_emocional/` está presente, el backend **usa automáticamente tu modelo entrenado** para reemplazar reglas manuales.

---

## 🧪 Pruebas automáticas

```bash
pytest tests/
```

Incluye pruebas de endpoints y lógica interna.

---

## 🐳 Docker

```dockerfile
docker build -t diario-backend .
docker run -p 5000:5000 diario-backend
```

---

## 📂 Estructura del Proyecto

- `main.py` – Lanza la app
- `app/` – Rutas y autenticación
- `services/` – Análisis, emociones, diagnóstico, estadísticas
- `data/` – SQLite DB
- `core/` – JWT
- `frontend.html` – Interfaz mínima
- `fine_tune_emotions.py` – Entrena IA
- `predict_emotion.py` – Predice emociones
- `tests/` – Pruebas unitarias

---

Creado con ❤️ para salud mental y tecnología.

---
## 🚀 Deploy Backend con Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/tu-usuario/diario-backend)

> 🚨 Reemplaza `https://github.com/tu-usuario/diario-backend` con el link real de tu repo
