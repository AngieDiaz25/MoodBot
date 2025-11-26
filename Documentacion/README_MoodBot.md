
# 🧠 MoodBot — Detección y Seguimiento de Estado Emocional en Texto

## 💬 Descripción general

**MoodBot** es un sistema inteligente basado en *Machine Learning* y *Procesamiento del Lenguaje Natural (NLP)* que analiza textos escritos por usuarios para detectar señales de **depresión, ansiedad o estados emocionales generales**.  

Combina dos componentes principales:
- 🤖 **Chatbot empático:** interactúa con el usuario y analiza el tono emocional en tiempo real.  
- 📊 **Mood Tracker:** registra los estados emocionales detectados y muestra su evolución a lo largo del tiempo.  

El objetivo principal es **promover el bienestar emocional** y demostrar el uso responsable de la inteligencia artificial en el análisis del lenguaje humano.

---

## 🎯 Objetivos

1. Desarrollar un modelo NLP capaz de identificar emociones o señales de ansiedad/depresión en texto.  
2. Implementar un sistema conversacional que interactúe con el usuario de forma empática.  
3. Registrar las emociones detectadas y visualizar la evolución del estado emocional a lo largo del tiempo.  
4. Evaluar el rendimiento del modelo y su capacidad de generalización.

---

## ⚙️ Técnicas y metodología

| Etapa | Descripción | Herramientas |
|-------|--------------|---------------|
| **1. Adquisición de datos** | Obtención de datasets públicos con textos etiquetados por emociones. | `pandas`, `requests` |
| **2. Preprocesamiento** | Limpieza de texto, tokenización, lematización, eliminación de stopwords. | `nltk`, `spaCy` |
| **3. Representación de texto** | TF-IDF o *word embeddings* (`Word2Vec`, `BERT embeddings`). | `scikit-learn`, `transformers` |
| **4. Modelado** | Clasificadores supervisados: Logistic Regression, Random Forest, o modelos BERT. | `scikit-learn`, `xgboost`, `transformers` |
| **5. Evaluación** | Accuracy, F1-score, Recall, ROC-AUC. | `scikit-learn` |
| **6. Interfaz** | Chatbot y dashboard de evolución emocional. | `Streamlit`, `Gradio`, `Plotly` |

---

## 🔍 Tipo de problema

- **Tipo:** Clasificación supervisada  
- **Salida:** Clase emocional o estado (positivo, neutro, negativo / depresión / ansiedad / normal)  
- **Objetivo del modelo:** Inferir el estado emocional del usuario a partir de su texto  

---

## 🗂️ Datasets recomendados

| Dataset | Descripción | Fuente |
|----------|--------------|--------|
| **DAIC-WOZ** | Conversaciones etiquetadas con niveles de depresión. | [USC ICT Database](https://dcapswoz.ict.usc.edu/) |
| **GoEmotions (Google)** | Dataset con 27 emociones humanas. | [GoEmotions Dataset](https://github.com/google-research/goemotions) |
| **Emotion Dataset (Kaggle)** | Textos con emociones como *joy*, *anger*, *sadness*, etc. | [Kaggle](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp) |
| **Reddit Depression Dataset** | Publicaciones en foros sobre depresión y ansiedad. | [Kaggle](https://www.kaggle.com/datasets) |

> 💡 Recomendado comenzar con **GoEmotions** o **Emotion Dataset** por su limpieza y formato sencillo.

---

## 📈 Métricas de evaluación

- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC-AUC  
- Evolución temporal del estado emocional promedio  

---

## 🧠 Nivel de complejidad

🔹 **Intermedio**, ideal para proyecto final o demostración práctica de técnicas NLP.  
Incluye procesamiento de texto, entrenamiento supervisado, interfaz interactiva y visualización.

---

## 🌍 Impacto social

MoodBot contribuye al **bienestar emocional digital** mediante el análisis ético del lenguaje.  
No sustituye una evaluación profesional, pero puede ayudar a **detectar patrones tempranos de tristeza, ansiedad o baja motivación**.

---

## 🧱 Arquitectura general

```
Usuario → Chatbot → Análisis NLP → Clasificador Emocional → Registro BD → Dashboard de Estado de Ánimo
```

### Componentes
- **Frontend:** Chat / Dashboard (Streamlit o Gradio)  
- **Backend:** Python (Flask o Streamlit)  
- **Modelo ML:** Clasificador emocional (TF-IDF + SVM / BERT)  
- **Almacenamiento:** CSV o SQLite (histórico de emociones)  
- **Visualización:** Plotly, Matplotlib o Seaborn  

---

## 🧩 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu_usuario/MoodBot.git
cd MoodBot

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## 🚀 Ejecución

```bash
# Ejecutar el chatbot (ejemplo con Streamlit)
streamlit run app.py
```

Luego abre el enlace local (por ejemplo: http://localhost:8501) y comienza a interactuar con **MoodBot**.

---

## 📊 Resultados esperados

- Un chatbot que analiza mensajes y responde empáticamente.  
- Gráficos del estado emocional del usuario a lo largo del tiempo.  
- Un modelo de NLP con F1-score > 0.80 sobre dataset limpio.  

---

## 🧱 Estructura del proyecto

```
MoodBot/
│
├── data/                     # Datasets utilizados
├── models/                   # Modelos entrenados
├── app.py                    # Chatbot o dashboard Streamlit
├── notebook_ML.ipynb         # Notebook con entrenamiento del modelo
├── requirements.txt          # Dependencias
├── README.md                 # Este documento
└── assets/                   # Imágenes, gráficos o logos
```

---

## 🔮 Extensiones futuras

- Integración con redes sociales (Twitter, Reddit, etc.)  
- Análisis multimodal (texto + voz)  
- Recomendación de recursos de bienestar (música, meditación, artículos)  
- Versión móvil con seguimiento emocional diario  

---

## 👥 Autores

**Angie Díaz**  
Proyecto de *Machine Learning aplicado a bienestar emocional*.  
The Bridge | Data Science Bootcamp 2025

---

## ⚠️ Nota ética

Este sistema **no reemplaza la ayuda profesional** en salud mental.  
Los resultados deben interpretarse como indicadores informativos y no diagnósticos médicos.
