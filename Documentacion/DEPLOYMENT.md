# 🚀 MoodBot - Guía de Deployment

## Tabla de Contenidos

1. [Pre-requisitos](#pre-requisitos)
2. [Preparación del Proyecto](#preparación-del-proyecto)
3. [Deployment Local](#deployment-local)
4. [Deployment en Render](#deployment-en-render)
5. [Deployment Frontend en Vercel](#deployment-frontend-en-vercel)
6. [Configuración de Variables de Entorno](#configuración-de-variables-de-entorno)
7. [Monitoreo y Mantenimiento](#monitoreo-y-mantenimiento)
8. [Troubleshooting](#troubleshooting)
9. [Mejores Prácticas](#mejores-prácticas)

---

## 1. Pre-requisitos

### Herramientas Necesarias

```bash
✓ Python 3.8 o superior
✓ Git
✓ Cuenta en GitHub
✓ Cuenta en Render (gratuita)
✓ Cuenta en Vercel (gratuita)
```

### Verificar Instalaciones

```bash
# Verificar Python
python --version
# Debería mostrar: Python 3.8.x o superior

# Verificar Git
git --version
# Debería mostrar: git version 2.x.x

# Verificar pip
pip --version
# Debería mostrar: pip 20.x.x o superior
```

---

## 2. Preparación del Proyecto

### 2.1 Estructura del Proyecto

```
moodbot-api/
├── app.py                    # Aplicación Flask
├── requirements.txt          # Dependencias
├── render.yaml              # Configuración Render
├── README.md                # Documentación
├── .gitignore               # Archivos ignorados por Git
├── models/
│   ├── best_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── model_metadata.pkl
└── tests/
    └── test_api.py
```

### 2.2 Crear requirements.txt

```bash
# requirements.txt
Flask==2.3.0
scikit-learn==1.3.0
nltk==3.8.1
pandas==2.0.3
numpy==1.24.3
joblib==1.3.0
gunicorn==21.2.0
```

**Notas importantes**:
- Versiones deben coincidir con las usadas en entrenamiento
- `gunicorn` es necesario para producción
- NLTK requiere descarga de datos adicionales

### 2.3 Crear .gitignore

```bash
# .gitignore
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
dist/
*.egg-info/
.DS_Store
.vscode/
.idea/
*.log
```

### 2.4 Configurar app.py para Producción

```python
# app.py
import os
from flask import Flask, request, jsonify
import joblib
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Descargar datos de NLTK (solo primera vez)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)

app = Flask(__name__)

# Cargar modelos
try:
    model = joblib.load('models/best_model.pkl')
    vectorizer = joblib.load('models/tfidf_vectorizer.pkl')
    MODEL_LOADED = True
except Exception as e:
    print(f"Error cargando modelos: {e}")
    MODEL_LOADED = False

lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """Preprocesa el texto de entrada"""
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)

@app.route('/')
def home():
    """Endpoint principal con información de la API"""
    return jsonify({
        'message': 'MoodBot API - Clasificador de Estados Emocionales',
        'version': '1.0.0',
        'endpoints': {
            'health': '/health',
            'predict': '/predict (POST)'
        }
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy' if MODEL_LOADED else 'unhealthy',
        'model_loaded': MODEL_LOADED
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint de predicción"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'No se proporcionó texto para analizar'}), 400
        
        text = data['text']
        if not text.strip():
            return jsonify({'error': 'El texto no puede estar vacío'}), 400
        
        # Preprocesar y predecir
        processed_text = preprocess_text(text)
        X = vectorizer.transform([processed_text])
        prediction = model.predict(X)[0]
        probabilities = model.predict_proba(X)[0]
        
        # Mapear probabilidades a clases
        classes = model.classes_
        prob_dict = {cls: float(prob) for cls, prob in zip(classes, probabilities)}
        
        # Generar mensaje empático
        messages = {
            'Neutral': [
                "¡Genial! Pareces estar en un buen estado emocional.",
                "Tu mensaje refleja estabilidad emocional. ¡Sigue así!"
            ],
            'Anxiety': [
                "Noto que estás experimentando ansiedad. Recuerda que es normal sentirse así a veces.",
                "Detecté signos de ansiedad. Las técnicas de respiración profunda pueden ayudar."
            ],
            'Depression': [
                "Noto que podrías estar pasando por un momento difícil. Considera hablar con alguien de confianza.",
                "Parece que te sientes desanimado/a. Recuerda que no estás solo/a."
            ]
        }
        
        import random
        message = random.choice(messages.get(prediction, ["Estado emocional detectado"]))
        
        return jsonify({
            'prediction': prediction,
            'confidence': float(max(probabilities)),
            'probabilities': prob_dict,
            'message': message,
            'input_text': text
        })
    
    except Exception as e:
        return jsonify({'error': f'Error al procesar la predicción: {str(e)}'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

---

## 3. Deployment Local

### 3.1 Configurar Entorno Virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

### 3.2 Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3.3 Ejecutar Localmente

```bash
python app.py
```

La API estará disponible en `http://localhost:5000`

### 3.4 Probar Endpoints Localmente

```bash
# Health check
curl http://localhost:5000/health

# Predicción
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Me siento muy bien hoy"}'
```

---

## 4. Deployment en Render

### 4.1 Preparar Repositorio Git

```bash
# Inicializar repositorio (si no existe)
git init

# Añadir archivos
git add .

# Commit inicial
git commit -m "Initial commit - MoodBot API"
```

### 4.2 Subir a GitHub

#### Opción A: GitHub CLI (Recomendado)

```bash
# Instalar GitHub CLI si no lo tienes
# Windows: winget install GitHub.cli
# Mac: brew install gh
# Linux: sudo apt install gh

# Autenticar
gh auth login

# Crear repositorio y subir código
gh repo create moodbot-api --public --source=. --remote=origin --push
```

#### Opción B: Manual

```bash
# Crear repo en github.com primero, luego:
git remote add origin https://github.com/TU_USUARIO/moodbot-api.git
git branch -M main
git push -u origin main
```

### 4.3 Crear render.yaml

```yaml
# render.yaml
services:
  - type: web
    name: moodbot-api
    env: python
    plan: free
    buildCommand: |
      pip install -r requirements.txt
      python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet'); nltk.download('omw-1.4')"
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

**Explicación**:
- `type: web` - Servicio web HTTP
- `env: python` - Runtime de Python
- `plan: free` - Plan gratuito (suficiente para empezar)
- `buildCommand` - Instala dependencias y datos de NLTK
- `startCommand` - Ejecuta app con gunicorn

### 4.4 Desplegar en Render

#### Paso 1: Crear Cuenta

1. Ve a [render.com](https://render.com)
2. Regístrate con GitHub
3. Autoriza Render para acceder a tus repos

#### Paso 2: Crear Web Service

1. Click en "New +" → "Web Service"
2. Conecta tu repositorio `moodbot-api`
3. Render detectará automáticamente `render.yaml`
4. Click en "Create Web Service"

#### Paso 3: Verificar Build

```
==> Building... 
Installing dependencies...
Downloading NLTK data...
==> Build successful!
==> Starting service...
Your service is live at https://moodbot-api.onrender.com
```

### 4.5 Verificar Deployment

```bash
# Health check
curl https://moodbot-api.onrender.com/health

# Debería retornar:
# {"status": "healthy", "model_loaded": true}
```

---

## 5. Deployment Frontend en Vercel

### 5.1 Estructura del Proyecto Frontend

```
moodbot-frontend/
├── index.html
├── styles.css
├── script.js
├── package.json          # Si usas React/Next.js
└── vercel.json          # Configuración Vercel
```

### 5.2 Ejemplo de Frontend Básico (HTML/JS)

#### index.html

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MoodBot - Análisis Emocional</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>🤖 MoodBot</h1>
        <p class="subtitle">Clasificador de Estados Emocionales</p>
        
        <div class="chat-box">
            <textarea 
                id="userInput" 
                placeholder="Cuéntame cómo te sientes..."
                rows="4"
            ></textarea>
            
            <button id="analyzeBtn" onclick="analyzeMood()">
                Analizar Estado Emocional
            </button>
            
            <div id="result" class="result"></div>
        </div>
    </div>
    
    <script src="script.js"></script>
</body>
</html>
```

#### script.js

```javascript
const API_URL = 'https://moodbot-api.onrender.com/predict';

async function analyzeMood() {
    const userInput = document.getElementById('userInput').value;
    const resultDiv = document.getElementById('result');
    
    if (!userInput.trim()) {
        resultDiv.innerHTML = '<p class="error">Por favor, escribe algo primero.</p>';
        return;
    }
    
    // Mostrar loading
    resultDiv.innerHTML = '<p class="loading">Analizando...</p>';
    
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: userInput })
        });
        
        if (!response.ok) {
            throw new Error('Error en la API');
        }
        
        const data = await response.json();
        
        // Mostrar resultado
        const emoji = {
            'Neutral': '🟢',
            'Anxiety': '🟡',
            'Depression': '🔴'
        }[data.prediction];
        
        resultDiv.innerHTML = `
            <div class="result-card ${data.prediction.toLowerCase()}">
                <h2>${emoji} ${data.prediction}</h2>
                <p class="confidence">Confianza: ${(data.confidence * 100).toFixed(1)}%</p>
                <p class="message">${data.message}</p>
                
                <details>
                    <summary>Ver probabilidades detalladas</summary>
                    <ul class="probabilities">
                        ${Object.entries(data.probabilities)
                            .map(([cls, prob]) => 
                                `<li>${cls}: ${(prob * 100).toFixed(1)}%</li>`
                            ).join('')}
                    </ul>
                </details>
            </div>
        `;
    } catch (error) {
        resultDiv.innerHTML = `<p class="error">Error: ${error.message}</p>`;
    }
}
```

### 5.3 Desplegar en Vercel

#### Opción A: Vercel CLI

```bash
# Instalar Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
cd moodbot-frontend
vercel --prod
```

#### Opción B: GitHub Integration (Recomendado)

1. Sube tu frontend a GitHub
2. Ve a [vercel.com](https://vercel.com)
3. Click "Import Project"
4. Selecciona tu repo
5. Click "Deploy"

### 5.4 Configurar vercel.json

```json
{
  "version": 2,
  "builds": [
    {
      "src": "index.html",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/$1"
    }
  ]
}
```

---

## 6. Configuración de Variables de Entorno

### 6.1 En Render

```bash
# Dashboard → Settings → Environment

# Variables sugeridas:
PYTHON_VERSION=3.11.0
FLASK_ENV=production
LOG_LEVEL=info
```

### 6.2 En Vercel

```bash
# Dashboard → Settings → Environment Variables

# Variables sugeridas:
NEXT_PUBLIC_API_URL=https://moodbot-api.onrender.com
NODE_ENV=production
```

### 6.3 Uso en Código

```python
# En Python (app.py)
import os

DEBUG = os.environ.get('FLASK_ENV', 'development') != 'production'
PORT = int(os.environ.get('PORT', 5000))
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'info')
```

```javascript
// En JavaScript
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000';
```

---

## 7. Monitoreo y Mantenimiento

### 7.1 Logs en Render

```bash
# Dashboard → Logs
# Ver logs en tiempo real
# Buscar errores con Ctrl+F
```

**Errores comunes en logs**:
```
❌ ModuleNotFoundError: No module named 'sklearn'
   → Verifica requirements.txt

❌ FileNotFoundError: [Errno 2] No such file or directory: 'models/best_model.pkl'
   → Asegúrate de que los modelos estén en Git

❌ Resource Lookup Error: punkt not found
   → Ejecuta descarga de NLTK en buildCommand
```

### 7.2 Monitoreo de Uptime

Usar servicios gratuitos de monitoreo:

**UptimeRobot** (Recomendado):
1. Crear cuenta en uptimerobot.com
2. Añadir monitor HTTP(s)
3. URL: `https://moodbot-api.onrender.com/health`
4. Intervalo: 5 minutos
5. Alerta por email si cae

### 7.3 Analytics

```python
# Añadir logging básico en app.py
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    logger.info(f"[{datetime.now()}] Nueva predicción recibida")
    # ... resto del código
    logger.info(f"[{datetime.now()}] Predicción: {prediction}")
```

---

## 8. Troubleshooting

### 8.1 Problemas Comunes

#### Problema: API no responde

```bash
# Diagnóstico
curl -I https://moodbot-api.onrender.com/health

# Soluciones:
1. Verificar que el servicio está "Running" en Render dashboard
2. Revisar logs para errores
3. Verificar que gunicorn está configurado correctamente
```

#### Problema: Cold Start lento

**Síntoma**: Primera petición tarda 20-30 segundos

**Causa**: Render free tier duerme servicios inactivos

**Soluciones**:
1. Usar plan pagado ($7/mes)
2. Implementar "keep-alive" ping cada 10 minutos
3. Advertir a usuarios sobre primer uso

```python
# keep_alive.py (ejecutar localmente)
import requests
import time

while True:
    try:
        requests.get('https://moodbot-api.onrender.com/health')
        print(f"Ping successful at {time.ctime()}")
    except:
        print(f"Ping failed at {time.ctime()}")
    time.sleep(600)  # 10 minutos
```

#### Problema: Modelo no se carga

```python
# Error típico:
FileNotFoundError: [Errno 2] No such file or directory: 'models/best_model.pkl'

# Solución:
1. Verificar que modelos están en Git:
   git ls-files models/

2. Si falta, añadir:
   git add models/*.pkl
   git commit -m "Add model files"
   git push

3. Trigger rebuild en Render
```

### 8.2 Testing del Deployment

```bash
# Script de test completo
#!/bin/bash

API_URL="https://moodbot-api.onrender.com"

echo "1. Testing health endpoint..."
curl $API_URL/health

echo -e "\n2. Testing root endpoint..."
curl $API_URL/

echo -e "\n3. Testing prediction - Neutral..."
curl -X POST $API_URL/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Hoy fue un día normal"}'

echo -e "\n4. Testing prediction - Anxiety..."
curl -X POST $API_URL/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Estoy muy nervioso y preocupado"}'

echo -e "\n5. Testing prediction - Depression..."
curl -X POST $API_URL/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Me siento muy triste y sin energía"}'

echo -e "\n✅ All tests completed!"
```

---

## 9. Mejores Prácticas

### 9.1 Seguridad

```python
# 1. Limitar tamaño de input
MAX_TEXT_LENGTH = 5000

@app.route('/predict', methods=['POST'])
def predict():
    text = data['text']
    if len(text) > MAX_TEXT_LENGTH:
        return jsonify({'error': 'Texto demasiado largo'}), 400

# 2. Rate limiting (opcional, requiere Flask-Limiter)
from flask_limiter import Limiter

limiter = Limiter(
    app,
    key_func=lambda: request.remote_addr,
    default_limits=["100 per hour"]
)

@app.route('/predict', methods=['POST'])
@limiter.limit("10 per minute")
def predict():
    # ...
```

### 9.2 Performance

```python
# 1. Cache del modelo (ya implementado con carga al inicio)
# 2. Comprimir respuestas
from flask_compress import Compress
Compress(app)

# 3. CORS para frontend
from flask_cors import CORS
CORS(app, resources={r"/*": {"origins": ["https://moodbot.vercel.app"]}})
```

### 9.3 CI/CD

```yaml
# .github/workflows/deploy.yml
name: Deploy to Render

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Run tests
        run: |
          pytest tests/
      
      - name: Deploy to Render
        run: |
          curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

### 9.4 Backups

```bash
# Backup de modelos
#!/bin/bash
DATE=$(date +%Y%m%d)
tar -czf models_backup_$DATE.tar.gz models/
# Subir a Google Drive, Dropbox, etc.
```

---

## 🎯 Checklist de Deployment

### Pre-Deployment
- [ ] Código probado localmente
- [ ] requirements.txt actualizado
- [ ] .gitignore configurado
- [ ] Modelos incluidos en Git
- [ ] README.md completo
- [ ] Tests pasando

### Deployment
- [ ] Código en GitHub
- [ ] render.yaml configurado
- [ ] Servicio creado en Render
- [ ] Build exitoso
- [ ] Health check funciona
- [ ] Endpoints probados

### Post-Deployment
- [ ] Monitoreo configurado
- [ ] Frontend conectado
- [ ] Documentación actualizada
- [ ] Team notificado
- [ ] Backup de modelos

---

## 📞 Soporte

¿Problemas con el deployment?

1. Revisa esta guía
2. Consulta logs de Render
3. Abre issue en GitHub
4. Contacta a [@AngieDiaz25](https://github.com/AngieDiaz25)

---

<div align="center">

**MoodBot Deployment Guide v1.0.0**  
Última actualización: Noviembre 2024

</div>
