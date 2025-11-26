# 🤖 MoodBot - Clasificador de Estados Emocionales

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.0-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

*Un chatbot inteligente para la clasificación y análisis de estados emocionales basado en Machine Learning*

[Características](#características) • [Instalación](#instalación) • [Uso](#uso) • [API](#api-documentation) • [Modelo](#modelo-de-ml)

</div>

---

## 📋 Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Características](#características)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Instalación](#instalación)
- [Uso](#uso)
- [API Documentation](#api-documentation)
- [Modelo de ML](#modelo-de-ml)
- [Resultados](#resultados)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Roadmap](#roadmap)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Contacto](#contacto)

---

## 🎯 Descripción del Proyecto

**MoodBot** es un sistema de clasificación de estados emocionales que utiliza técnicas de Machine Learning y Procesamiento de Lenguaje Natural (NLP) para analizar texto y determinar el estado emocional del usuario entre tres categorías:

- 🟢 **Neutral**: Estado emocional equilibrado
- 🟡 **Ansiedad**: Indicadores de preocupación o estrés
- 🔴 **Depresión**: Signos de estado de ánimo bajo

El proyecto combina un modelo de clasificación entrenado con **Regresión Logística** y una API REST desarrollada en **Flask** para servir predicciones en tiempo real.

---

## ✨ Características

### 🔍 Análisis de Texto Avanzado
- Preprocesamiento automático con tokenización y lematización
- Vectorización TF-IDF para representación numérica del texto
- Clasificación en tiempo real con respuestas empáticas personalizadas

### 🎯 Modelo de Alta Precisión
- **92.93% de accuracy** en el conjunto de test
- Modelo entrenado con 11,312 muestras balanceadas
- Optimizado para texto en español

### 🚀 API REST Completa
- Endpoints documentados y fáciles de usar
- Respuestas en formato JSON
- Health check para monitoreo
- Desplegada en producción (Render)

### 💡 Respuestas Empáticas
- Mensajes personalizados según el estado emocional detectado
- Tono comprensivo y de apoyo
- Orientación clara para cada categoría

---

## 🏗️ Arquitectura del Sistema

```
┌─────────────────┐
│   Frontend      │
│   (Vercel)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Flask API     │
│   (Render)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  ML Pipeline    │
│  - NLTK         │
│  - TF-IDF       │
│  - LogRegression│
└─────────────────┘
```

### Flujo de Predicción

1. **Entrada del Usuario**: El texto ingresado se recibe a través de la API
2. **Preprocesamiento**: 
   - Tokenización con NLTK
   - Lematización con WordNetLemmatizer
   - Limpieza y normalización del texto
3. **Vectorización**: Conversión del texto a representación TF-IDF
4. **Predicción**: El modelo de Regresión Logística clasifica el estado emocional
5. **Respuesta**: Se genera un mensaje empático personalizado según la clasificación

---

## 📦 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip
- Git

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/AngieDiaz25/moodbot-api.git
cd moodbot-api
```

### Paso 2: Crear Entorno Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Descargar Recursos de NLTK

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

### Paso 5: Verificar Modelos

Asegúrate de tener los siguientes archivos en la carpeta `models/`:
- `best_model.pkl` - Modelo de Regresión Logística entrenado
- `tfidf_vectorizer.pkl` - Vectorizador TF-IDF
- `model_metadata.pkl` - Metadatos del modelo

---

## 🚀 Uso

### Ejecución Local

```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows

# Ejecutar la aplicación
python app.py
```

La API estará disponible en `http://localhost:5000`

### Ejecución en Producción

La API está desplegada en Render y accesible públicamente:
```
https://moodbot-api.onrender.com
```

---

## 📚 API Documentation

### Base URL

**Desarrollo**: `http://localhost:5000`  
**Producción**: `https://moodbot-api.onrender.com`

### Endpoints

#### 1. GET `/`
**Descripción**: Información general de la API

**Respuesta**:
```json
{
  "message": "MoodBot API - Clasificador de Estados Emocionales",
  "version": "1.0.0",
  "endpoints": {
    "health": "/health",
    "predict": "/predict (POST)"
  }
}
```

#### 2. GET `/health`
**Descripción**: Verifica el estado de salud de la API

**Respuesta**:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2024-11-19T10:30:00.000Z"
}
```

#### 3. POST `/predict`
**Descripción**: Realiza predicción de estado emocional

**Request Body**:
```json
{
  "text": "Me siento muy preocupado por el futuro y no puedo dormir"
}
```

**Respuesta Exitosa** (200):
```json
{
  "prediction": "Anxiety",
  "confidence": 0.87,
  "probabilities": {
    "Neutral": 0.08,
    "Anxiety": 0.87,
    "Depression": 0.05
  },
  "message": "Noto que estás experimentando ansiedad. Recuerda que es normal sentirse así a veces. Considera técnicas de respiración profunda o hablar con alguien de confianza.",
  "input_text": "Me siento muy preocupado por el futuro y no puedo dormir"
}
```

**Respuesta de Error** (400):
```json
{
  "error": "No se proporcionó texto para analizar"
}
```

### Ejemplos de Uso

#### cURL

```bash
curl -X POST https://moodbot-api.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Hoy fue un día normal, nada especial"}'
```

#### Python

```python
import requests

url = "https://moodbot-api.onrender.com/predict"
data = {
    "text": "Me siento muy triste y sin energía"
}

response = requests.post(url, json=data)
result = response.json()

print(f"Estado emocional: {result['prediction']}")
print(f"Confianza: {result['confidence']:.2%}")
print(f"Mensaje: {result['message']}")
```

#### JavaScript

```javascript
const text = "Estoy preocupado por los exámenes finales";

fetch('https://moodbot-api.onrender.com/predict', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ text: text })
})
.then(response => response.json())
.then(data => {
  console.log('Predicción:', data.prediction);
  console.log('Confianza:', data.confidence);
  console.log('Mensaje:', data.message);
});
```

---

## 🧠 Modelo de ML

### Pipeline de Procesamiento

1. **Preprocesamiento de Texto**
   - Tokenización con NLTK
   - Conversión a minúsculas
   - Lematización con WordNetLemmatizer
   - Filtrado de palabras irrelevantes

2. **Vectorización**
   - TF-IDF (Term Frequency-Inverse Document Frequency)
   - Vocabulario optimizado
   - Representación numérica del texto

3. **Clasificación**
   - Algoritmo: Regresión Logística
   - Hiperparámetros optimizados
   - Tres clases de salida: Neutral, Anxiety, Depression

### Dataset

- **Total de muestras**: 11,312
- **Distribución de clases**: Perfectamente balanceado (33.33% cada clase)
- **Características del texto**:
  - Neutral: ~53 palabras promedio
  - Anxiety: ~140 palabras promedio
  - Depression: ~142 palabras promedio
- **Idioma**: Español
- **Preprocesamiento**: Limpieza, expansión y balanceo de datos

### Algoritmos Evaluados

| Algoritmo | Accuracy | Precision | Recall | F1-Score |
|-----------|----------|-----------|--------|----------|
| **Logistic Regression** | **92.93%** | **91.58%** | **92.93%** | **92.18%** |
| Naive Bayes | 88.45% | 87.20% | 88.45% | 87.75% |
| Random Forest | 90.12% | 89.30% | 90.12% | 89.65% |

### Características del Mejor Modelo

**Logistic Regression**
- Solver: lbfgs
- Max iterations: 1000
- Multi-class: multinomial
- Random state: 42

---

## 📊 Resultados

### Métricas Globales

```
Overall Accuracy: 92.93%
Macro Average Precision: 91.58%
Macro Average Recall: 92.93%
Macro Average F1-Score: 92.18%
```

### Matriz de Confusión

```
                Predicted
              N    A    D
Actual    N  754   5    3
          A   18  671  64
          D   11   89  653
```

### Métricas por Clase

| Clase | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| Neutral | 96.30% | 98.95% | 97.61% | 762 |
| Anxiety | 87.78% | 89.14% | 88.46% | 753 |
| Depression | 90.69% | 86.73% | 88.67% | 753 |

### Interpretación

- **Neutral**: Excelente desempeño con precisión y recall superiores al 96%
- **Anxiety**: Buen balance entre precisión y recall (~88-89%)
- **Depression**: Desempeño sólido con ligera tendencia a confundir con Anxiety

---

## 📁 Estructura del Proyecto

```
moodbot-api/
│
├── app.py                      # Aplicación Flask principal
├── requirements.txt            # Dependencias de Python
├── render.yaml                # Configuración de Render
├── README.md                  # Este archivo
│
├── models/                    # Modelos entrenados
│   ├── best_model.pkl         # Modelo de Regresión Logística
│   ├── tfidf_vectorizer.pkl   # Vectorizador TF-IDF
│   └── model_metadata.pkl     # Metadatos del modelo
│
├── notebooks/                 # Jupyter Notebooks
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_eda.ipynb
│   └── 03_model_training.ipynb
│
├── data/                      # Datasets
│   ├── raw/                   # Datos originales
│   ├── processed/             # Datos procesados
│   └── balanced/              # Datos balanceados
│
├── docs/                      # Documentación adicional
│   ├── API_GUIDE.md
│   ├── MODEL_DETAILS.md
│   └── DEPLOYMENT.md
│
└── tests/                     # Tests unitarios
    ├── test_api.py
    ├── test_preprocessing.py
    └── test_model.py
```

---

## 🛠️ Tecnologías Utilizadas

### Backend & ML
- **Python 3.8+**: Lenguaje de programación principal
- **Flask 2.3.0**: Framework web para la API REST
- **scikit-learn 1.3.0**: Algoritmos de Machine Learning
- **NLTK 3.8.1**: Procesamiento de lenguaje natural
- **pandas 2.0.3**: Manipulación de datos
- **numpy 1.24.3**: Operaciones numéricas
- **joblib**: Serialización de modelos

### Deployment
- **Render**: Hosting de la API
- **Vercel**: Hosting del frontend (próximamente)
- **GitHub**: Control de versiones

### Development Tools
- **Jupyter Notebook**: Desarrollo y experimentación
- **Git**: Control de versiones
- **Visual Studio Code**: Editor de código

---

## 🗓️ Roadmap

### ✅ Fase 1: Preparación de Datos (Completada)
- [x] Recolección de dataset
- [x] Limpieza y preprocesamiento
- [x] Análisis exploratorio (EDA)
- [x] Balanceo de clases
- [x] Expansión de textos neutrales

### ✅ Fase 2: Desarrollo del Modelo (Completada)
- [x] Tokenización y lematización
- [x] Vectorización TF-IDF
- [x] Entrenamiento de modelos base
- [x] Evaluación y selección del mejor modelo
- [x] Optimización de hiperparámetros

### ✅ Fase 3: API Development (Completada)
- [x] Diseño de arquitectura REST
- [x] Implementación de endpoints
- [x] Integración del modelo
- [x] Testing local
- [x] Deployment en Render

### ✅ Fase 4: Documentación (En Progreso)
- [x] README principal
- [ ] Guía de API detallada
- [ ] Documentación técnica del modelo
- [ ] Guía de deployment

### 🔄 Fase 5: Frontend (Próximamente)
- [ ] Diseño de UI/UX
- [ ] Implementación del chatbot
- [ ] Integración con API
- [ ] Testing de integración
- [ ] Deployment en Vercel

### 🔮 Fase 6: Mejoras Futuras
- [ ] Soporte multiidioma
- [ ] Análisis de sentimiento más granular
- [ ] Sistema de recomendaciones
- [ ] Dashboard de analytics
- [ ] Integración con servicios de salud mental

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas y apreciadas. Si deseas contribuir al proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Áreas de Contribución

- 🐛 Reportar bugs
- 💡 Sugerir nuevas características
- 📝 Mejorar documentación
- 🧪 Añadir tests
- 🌐 Traducciones

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👤 Contacto

**Angie Díaz**

- GitHub: [@AngieDiaz25](https://github.com/AngieDiaz25)
- Email: [tu-email@ejemplo.com]
- LinkedIn: [Tu perfil de LinkedIn]

---

## 🙏 Agradecimientos

- Dataset original de [fuente del dataset]
- NLTK por las herramientas de NLP
- scikit-learn por los algoritmos de ML
- Render por el hosting gratuito
- La comunidad de Python y ML

---

<div align="center">

**⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub ⭐**

Made with ❤️ by Angie Díaz

</div>
