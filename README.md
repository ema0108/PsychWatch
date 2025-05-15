# 🧠 Diario Psicológico Inteligente - Backend & IA

**Sistema integral para el análisis emocional mediante IA y seguimiento terapéutico**  
*¡Colabora en este proyecto crucial para la salud mental! Últimos días para implementación.*

---

## 📌 Descripción
Plataforma web que permite a pacientes registrar sus estados emocionales diarios, analizándolos en tiempo real con modelos de lenguaje avanzados. Los psicólogos acceden a un panel interactivo con:
- 📈 Gráficos dinámicos de tendencias emocionales
- 🧩 Diagnósticos preliminares basados en IA
- 📋 Historial clínico automatizado
- 🔐 Sistema seguro de autenticación JWT

---

## 🚀 Características principales
| Módulo         | Tecnologías Clave                 | Funcionalidades                             |
|----------------|-----------------------------------|---------------------------------------------|
| **Backend**    | Flask, JWT, SQLite                | API REST, Autenticación, Gestión de datos   |
| **Frontend**   | HTML5, Chart.js, CSS3             | Dashboard interactivo, Visualización de datos |
| **IA**         | Transformers, PyTorch             | Modelo fine-tuned para clasificación emocional |
| **DevOps**     | Docker, Render.com                | Despliegue escalable, CI/CD ready           |

---

## 🛠 Instalación rápida
```bash
# 1. Clonar repositorio
git clone https://github.com/tu-usuario/diario-psicologico.git

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Inicializar base de datos
python -c "from data.db import init_db; init_db()"

# 4. Entrenar modelo IA (opcional)
python fine_tune_emotions.py --dataset dataset_emociones.csv

# 5. Ejecutar aplicación
python main.py
