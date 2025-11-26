# 📡 MoodBot API - Guía Completa

## Introducción

La API de MoodBot es un servicio REST que permite clasificar estados emocionales en texto. Esta guía proporciona información detallada sobre cómo integrar y utilizar la API en tus aplicaciones.

---

## 🌐 URLs Base

| Ambiente | URL | Descripción |
|----------|-----|-------------|
| **Producción** | `https://moodbot-api.onrender.com` | Servidor en producción, estable |
| **Desarrollo** | `http://localhost:5000` | Servidor local para desarrollo |

---

## 🔑 Autenticación

Actualmente, la API es de acceso público y **no requiere autenticación**. En futuras versiones, se implementará autenticación mediante API Keys.

---

## 📋 Endpoints Detallados

### 1. Root Endpoint

#### `GET /`

Obtiene información general sobre la API.

**Request**
```http
GET / HTTP/1.1
Host: moodbot-api.onrender.com
```

**Response** (200 OK)
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

**Ejemplo cURL**
```bash
curl https://moodbot-api.onrender.com/
```

**Ejemplo Python**
```python
import requests

response = requests.get('https://moodbot-api.onrender.com/')
print(response.json())
```

---

### 2. Health Check

#### `GET /health`

Verifica el estado de salud de la API y la disponibilidad del modelo.

**Request**
```http
GET /health HTTP/1.1
Host: moodbot-api.onrender.com
```

**Response** (200 OK)
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2024-11-19T10:30:00.000Z"
}
```

**Estados Posibles**

| Campo | Tipo | Valores Posibles | Descripción |
|-------|------|------------------|-------------|
| `status` | string | `"healthy"`, `"unhealthy"` | Estado general de la API |
| `model_loaded` | boolean | `true`, `false` | Si el modelo ML está cargado |
| `timestamp` | string | ISO 8601 | Momento de la verificación |

**Ejemplo cURL**
```bash
curl https://moodbot-api.onrender.com/health
```

**Ejemplo Python**
```python
import requests

response = requests.get('https://moodbot-api.onrender.com/health')
health = response.json()

if health['status'] == 'healthy' and health['model_loaded']:
    print("✅ API lista para usar")
else:
    print("❌ API no disponible")
```

**Uso Recomendado**
- Monitoreo de disponibilidad del servicio
- Health checks en aplicaciones
- Validación antes de realizar predicciones

---

### 3. Predict Endpoint (Principal)

#### `POST /predict`

Realiza la clasificación del estado emocional del texto proporcionado.

**Request**
```http
POST /predict HTTP/1.1
Host: moodbot-api.onrender.com
Content-Type: application/json

{
  "text": "texto a analizar"
}
```

**Headers Requeridos**
```
Content-Type: application/json
```

**Request Body**

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `text` | string | Sí | Texto a clasificar (mínimo 1 carácter) |

**Response Exitosa** (200 OK)
```json
{
  "prediction": "Anxiety",
  "confidence": 0.87,
  "probabilities": {
    "Neutral": 0.08,
    "Anxiety": 0.87,
    "Depression": 0.05
  },
  "message": "Noto que estás experimentando ansiedad. Recuerda que es normal sentirse así a veces.",
  "input_text": "Me siento muy preocupado por el futuro"
}
```

**Campos de Respuesta**

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `prediction` | string | Clase predicha: `"Neutral"`, `"Anxiety"`, o `"Depression"` |
| `confidence` | float | Confianza de la predicción (0.0 - 1.0) |
| `probabilities` | object | Probabilidades para cada clase |
| `message` | string | Mensaje empático personalizado |
| `input_text` | string | Texto analizado (eco) |

**Respuestas de Error**

**400 Bad Request** - Falta el campo "text"
```json
{
  "error": "No se proporcionó texto para analizar"
}
```

**400 Bad Request** - Texto vacío
```json
{
  "error": "El texto no puede estar vacío"
}
```

**500 Internal Server Error** - Error en el servidor
```json
{
  "error": "Error al procesar la predicción: [detalles del error]"
}
```

---

## 💬 Mensajes Empáticos por Categoría

La API genera mensajes personalizados según la clasificación:

### Neutral
Mensajes de refuerzo positivo:
- "¡Genial! Pareces estar en un buen estado emocional."
- "Tu mensaje refleja estabilidad emocional. ¡Sigue así!"
- "Todo parece estar en equilibrio. ¡Excelente!"

### Anxiety (Ansiedad)
Mensajes de apoyo y técnicas de manejo:
- "Noto que estás experimentando ansiedad. Recuerda que es normal sentirse así a veces."
- "Pareces estar preocupado/a. Considera tomar un respiro y hacer una pausa."
- "Detecté signos de ansiedad. Las técnicas de respiración profunda pueden ayudar."

### Depression (Depresión)
Mensajes de comprensión y sugerencias de ayuda:
- "Noto que podrías estar pasando por un momento difícil. Considera hablar con alguien de confianza."
- "Parece que te sientes desanimado/a. Recuerda que no estás solo/a."
- "Tu mensaje refleja tristeza. Es importante buscar apoyo cuando lo necesites."

---

## 📊 Ejemplos de Uso Completos

### Ejemplo 1: Texto Neutral

**Request**
```bash
curl -X POST https://moodbot-api.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hoy fue un día normal en el trabajo. Terminé mis tareas y ahora voy a descansar."
  }'
```

**Response**
```json
{
  "prediction": "Neutral",
  "confidence": 0.95,
  "probabilities": {
    "Neutral": 0.95,
    "Anxiety": 0.03,
    "Depression": 0.02
  },
  "message": "¡Genial! Pareces estar en un buen estado emocional.",
  "input_text": "Hoy fue un día normal en el trabajo..."
}
```

---

### Ejemplo 2: Texto con Ansiedad

**Request (Python)**
```python
import requests

url = "https://moodbot-api.onrender.com/predict"
data = {
    "text": "No puedo dejar de preocuparme por los exámenes. "
            "Me siento muy nervioso y no puedo concentrarme. "
            "Mi corazón late rápido y tengo dificultad para dormir."
}

response = requests.post(url, json=data)
result = response.json()

print(f"Predicción: {result['prediction']}")
print(f"Confianza: {result['confidence']:.2%}")
print(f"Mensaje: {result['message']}")
```

**Response**
```json
{
  "prediction": "Anxiety",
  "confidence": 0.91,
  "probabilities": {
    "Neutral": 0.04,
    "Anxiety": 0.91,
    "Depression": 0.05
  },
  "message": "Detecté signos de ansiedad. Las técnicas de respiración profunda pueden ayudar.",
  "input_text": "No puedo dejar de preocuparme..."
}
```

---

### Ejemplo 3: Texto con Depresión

**Request (JavaScript)**
```javascript
const text = "Me siento muy triste y sin energía. " +
             "No tengo ganas de hacer nada y todo me parece sin sentido. " +
             "He perdido interés en las cosas que antes me gustaban.";

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
  console.log('Probabilidades:', data.probabilities);
})
.catch(error => console.error('Error:', error));
```

**Response**
```json
{
  "prediction": "Depression",
  "confidence": 0.89,
  "probabilities": {
    "Neutral": 0.03,
    "Anxiety": 0.08,
    "Depression": 0.89
  },
  "message": "Noto que podrías estar pasando por un momento difícil. Considera hablar con alguien de confianza.",
  "input_text": "Me siento muy triste y sin energía..."
}
```

---

## 🔧 Integración en Diferentes Lenguajes

### Python (requests)

```python
import requests
import json

class MoodBotClient:
    def __init__(self, base_url="https://moodbot-api.onrender.com"):
        self.base_url = base_url
    
    def check_health(self):
        """Verifica el estado de la API"""
        response = requests.get(f"{self.base_url}/health")
        return response.json()
    
    def predict(self, text):
        """Realiza una predicción de estado emocional"""
        response = requests.post(
            f"{self.base_url}/predict",
            json={"text": text}
        )
        return response.json()
    
    def batch_predict(self, texts):
        """Predice múltiples textos"""
        results = []
        for text in texts:
            result = self.predict(text)
            results.append(result)
        return results

# Uso
client = MoodBotClient()

# Verificar salud
health = client.check_health()
print(f"API Status: {health['status']}")

# Predicción simple
result = client.predict("Me siento muy bien hoy")
print(f"Emoción: {result['prediction']}")

# Predicción por lotes
texts = [
    "Estoy muy preocupado",
    "Todo está bien",
    "Me siento triste"
]
results = client.batch_predict(texts)
for i, r in enumerate(results):
    print(f"{i+1}. {r['prediction']} ({r['confidence']:.2%})")
```

---

### JavaScript (Fetch API)

```javascript
class MoodBotAPI {
  constructor(baseURL = 'https://moodbot-api.onrender.com') {
    this.baseURL = baseURL;
  }

  async checkHealth() {
    const response = await fetch(`${this.baseURL}/health`);
    return await response.json();
  }

  async predict(text) {
    const response = await fetch(`${this.baseURL}/predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text })
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  }

  async batchPredict(texts) {
    const promises = texts.map(text => this.predict(text));
    return await Promise.all(promises);
  }
}

// Uso
const api = new MoodBotAPI();

// Verificar salud
api.checkHealth().then(health => {
  console.log('API Status:', health.status);
});

// Predicción simple
api.predict('Me siento genial').then(result => {
  console.log('Emoción:', result.prediction);
  console.log('Confianza:', result.confidence);
});

// Predicción por lotes
const texts = ['Estoy nervioso', 'Todo bien', 'Estoy triste'];
api.batchPredict(texts).then(results => {
  results.forEach((r, i) => {
    console.log(`${i+1}. ${r.prediction} (${(r.confidence * 100).toFixed(1)}%)`);
  });
});
```

---

### cURL

```bash
# Health Check
curl https://moodbot-api.onrender.com/health

# Predicción simple
curl -X POST https://moodbot-api.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Me siento preocupado"}'

# Predicción con formato bonito
curl -X POST https://moodbot-api.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Hoy fue un buen día"}' | jq '.'
```

---

## ⚠️ Mejores Prácticas

### 1. Validación de Entrada
```python
def validate_text(text):
    if not text or not text.strip():
        raise ValueError("El texto no puede estar vacío")
    
    if len(text) < 10:
        print("Advertencia: texto muy corto, la predicción puede ser menos precisa")
    
    if len(text) > 1000:
        print("Advertencia: texto muy largo, considera dividirlo")
    
    return text.strip()
```

### 2. Manejo de Errores
```python
def safe_predict(text):
    try:
        response = requests.post(
            "https://moodbot-api.onrender.com/predict",
            json={"text": text},
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.Timeout:
        return {"error": "Timeout: la API tardó demasiado"}
    
    except requests.exceptions.ConnectionError:
        return {"error": "No se pudo conectar a la API"}
    
    except requests.exceptions.HTTPError as e:
        return {"error": f"Error HTTP: {e.response.status_code}"}
    
    except Exception as e:
        return {"error": f"Error inesperado: {str(e)}"}
```

### 3. Reintentos con Backoff
```python
import time
from functools import wraps

def retry_with_backoff(retries=3, backoff_factor=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries - 1:
                        raise
                    wait_time = backoff_factor ** attempt
                    print(f"Intento {attempt + 1} falló. Reintentando en {wait_time}s...")
                    time.sleep(wait_time)
        return wrapper
    return decorator

@retry_with_backoff(retries=3)
def predict_with_retry(text):
    response = requests.post(
        "https://moodbot-api.onrender.com/predict",
        json={"text": text}
    )
    response.raise_for_status()
    return response.json()
```

---

## 📈 Limitaciones y Consideraciones

### Limitaciones Actuales
- **Sin autenticación**: API pública sin rate limiting
- **Idioma**: Optimizado solo para español
- **Longitud de texto**: Mejor rendimiento con 20-500 palabras
- **Cold start**: Primera petición puede tardar más (~30s en Render free tier)

### Consideraciones de Rendimiento
- **Latencia típica**: 200-500ms
- **Cold start**: 20-30 segundos (Render free tier)
- **Timeout recomendado**: 10 segundos

### Casos de Uso Recomendados
✅ Análisis de diario emocional  
✅ Chatbots de apoyo emocional  
✅ Sistemas de monitoreo de bienestar  
✅ Aplicaciones de salud mental  

❌ Diagnóstico médico profesional  
❌ Decisiones legales o financieras  
❌ Contextos donde se requiere 100% de precisión  

---

## 🚀 Próximas Características

- [ ] Autenticación con API Keys
- [ ] Rate limiting por usuario
- [ ] Soporte multiidioma
- [ ] Análisis de sentimiento más granular
- [ ] Webhooks para notificaciones
- [ ] Batch API para múltiples predicciones
- [ ] Streaming de respuestas
- [ ] Dashboard de analytics

---

## 🆘 Soporte

¿Problemas con la API?

1. Verifica el [Health Check](#2-health-check)
2. Revisa los [ejemplos de uso](#-ejemplos-de-uso-completos)
3. Consulta las [mejores prácticas](#️-mejores-prácticas)
4. Abre un issue en [GitHub](https://github.com/AngieDiaz25/moodbot-api/issues)

---

## 📝 Changelog

### v1.0.0 (2024-11-19)
- ✨ Lanzamiento inicial
- 🎯 Endpoint de predicción
- 💚 Health check
- 📊 Probabilidades por clase
- 💬 Mensajes empáticos

---

<div align="center">

**MoodBot API v1.0.0**  
Hecho con ❤️ por Angie Díaz

</div>
