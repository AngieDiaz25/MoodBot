# MoodBot - Sistema de Análisis Emocional

Sistema integral de análisis emocional que combina clasificación de Machine Learning con respuestas empáticas generadas por IA para proporcionar apoyo en salud mental y recursos contextuales.

## Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Características](#características)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Stack Tecnológico](#stack-tecnológico)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Documentación de la API](#documentación-de-la-api)
- [Rendimiento del Modelo](#rendimiento-del-modelo)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Despliegue](#despliegue)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Desarrollo](#desarrollo)
- [Pruebas](#pruebas)
- [Contribuir](#contribuir)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Descripción General

MoodBot es un sistema de clasificación de estados emocionales que analiza texto de entrada en español y proporciona:

- **Clasificación Emocional**: Categoriza estados emocionales en Neutro, Ansiedad o Depresión usando Machine Learning
- **Respuestas Empáticas**: Genera mensajes personalizados de apoyo usando Google Gemini AI
- **Recursos Contextuales**: Proporciona recursos de ayuda específicos por categoría incluyendo líneas de crisis, técnicas de respiración y recomendaciones de bienestar
- **Procesamiento Bilingüe**: Maneja entrada en español con procesamiento del modelo en inglés mediante traducción automática

**Versión Actual**: 2.0.0  
**Precisión del Modelo**: 92.93%  
**Estado**: Listo para producción

## Características

### Funcionalidad Principal

- **Clasificación con Machine Learning**
  - Modelo de Regresión Logística con 92.93% de precisión
  - Vectorización TF-IDF con 5,000 características
  - Análisis de n-gramas (unigramas y bigramas)
  - Pipeline de preprocesamiento NLTK

- **Respuestas Potenciadas por IA**
  - Integración con Google Gemini Pro
  - Mensajería empática consciente del contexto
  - Mecanismo de respaldo para confiabilidad
  - Ingeniería de prompts optimizada para apoyo en salud mental

- **Recursos de Ayuda Contextuales**
  - Depresión: Líneas de crisis 24/7 (024, Teléfono de la Esperanza, Cruz Roja)
  - Ansiedad: Técnicas de respiración (4-7-8), ejercicios de grounding, guía de mindfulness
  - Neutro: Recomendaciones preventivas de bienestar

- **Interfaz de Usuario**
  - Diseño responsive (escritorio, tablet, móvil)
  - Interfaz de chat en tiempo real
  - Funcionalidad de reinicio con clic
  - Visualización de recursos con formato y saltos de línea

### Aspectos Técnicos Destacados

- Arquitectura API RESTful
- Diseño sin estado para escalabilidad
- Traducción automática español-inglés
- Manejo robusto de errores
- CORS habilitado para integración con frontend
- Despliegue en producción en Railway y Vercel

## Arquitectura del Sistema

```
Entrada del Usuario (Español)
    |
    v
Frontend (Vercel) - HTML/CSS/JavaScript
    |
    v
API Gateway - Flask REST API
    |
    v
Capa de Traducción - deep-translator (ES -> EN)
    |
    v
Pipeline de Preprocesamiento - NLTK
    |
    v
Extracción de Características - Vectorización TF-IDF
    |
    v
Clasificación ML - Regresión Logística
    |
    v
Generación de Respuesta IA - Google Gemini Pro
    |
    v
Formato de Recursos - Ayuda específica por categoría
    |
    v
Respuesta JSON -> Frontend -> Usuario
```

### Flujo de Datos

1. **Procesamiento de Entrada**: Mensaje del usuario recibido en español
2. **Traducción**: Español a inglés para compatibilidad con el modelo
3. **Preprocesamiento**: Tokenización, eliminación de stopwords, stemming
4. **Vectorización**: Transformación TF-IDF (5,000 características)
5. **Clasificación**: Predicción de Regresión Logística con nivel de confianza
6. **Generación de Respuesta**: Gemini AI crea respuesta empática
7. **Adición de Recursos**: Recursos específicos por categoría añadidos
8. **Salida**: Respuesta JSON completa con clasificación y orientación

## Stack Tecnológico

### Backend

- **Framework**: Flask 3.0.0
- **Machine Learning**: scikit-learn 1.7.2
- **Procesamiento de Lenguaje Natural**: NLTK 3.8.1
- **Integración IA**: google-generativeai 0.3.2
- **Traducción**: deep-translator 1.11.4
- **Serialización de Modelos**: joblib 1.3.2
- **Servidor de Producción**: Gunicorn 23.0.0
- **Manejo de CORS**: flask-cors 4.0.0

### Frontend

- **Marcado**: HTML5
- **Estilos**: CSS3 (personalizado, sin frameworks)
- **Scripting**: JavaScript Vanilla (ES6+)
- **Fuentes**: Google Fonts (Inter)
- **Iconos**: Caracteres emoji Unicode

### DevOps y Despliegue

- **Hosting Backend**: Railway
- **Hosting Frontend**: Vercel
- **Control de Versiones**: Git/GitHub
- **CI/CD**: Despliegue automático al hacer push a rama main

### Herramientas de Desarrollo

- **Editor de Código**: Visual Studio Code
- **Pruebas de API**: cURL, Postman
- **DevTools de Navegador**: Chrome/Safari Inspector

## Instalación

### Prerequisitos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Git
- API key de Google Gemini (tier gratuito disponible)

### Configuración del Backend

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/AngieDiaz25/MoodBot.git
   cd MoodBot/moodbot-api
   ```

2. **Crear entorno virtual** (recomendado)
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Descargar datos de NLTK**
   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('omw-1.4')"
   ```

5. **Configurar variables de entorno**
   ```bash
   export GEMINI_API_KEY='tu_api_key_aqui'
   ```

6. **Ejecutar la aplicación**
   ```bash
   python app.py
   # O con Gunicorn:
   gunicorn app:app --bind 0.0.0.0:5000
   ```

La API estará disponible en `http://localhost:5000`

### Configuración del Frontend

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/AngieDiaz25/moodbot-frontend.git
   cd moodbot-frontend
   ```

2. **Abrir con servidor local**
   - Usando VS Code: Instalar extensión "Live Server" y hacer clic en "Go Live"
   - Usando Python: `python -m http.server 8000`
   - O simplemente abrir `index.html` en un navegador

3. **Actualizar endpoint de API** (si no se usa la URL de producción)
   - Editar `script.js`
   - Cambiar la constante `API_URL` a tu URL de backend local

## Configuración

### Variables de Entorno

**Backend (Railway)**

| Variable | Descripción | Requerida |
|----------|-------------|-----------|
| `GEMINI_API_KEY` | API key de Google Gemini Pro | Sí |
| `PORT` | Puerto de la aplicación (auto-configurado por Railway) | No |

### Obtener API Key de Gemini

1. Visitar [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Iniciar sesión con cuenta de Google
3. Hacer clic en "Create API Key"
4. Seleccionar o crear un proyecto
5. Copiar la API key generada
6. Añadir a variables de entorno de Railway o archivo local `.env`

**Nota**: El tier gratuito proporciona 60 solicitudes por minuto, suficiente para desarrollo y producción a pequeña escala.

## Documentación de la API

### URL Base

**Producción**: `https://moodbot-production.up.railway.app`  
**Local**: `http://localhost:5000`

### Endpoints

#### Verificación de Estado

```http
GET /health
```

**Respuesta**
```json
{
  "status": "healthy",
  "models_loaded": true,
  "gemini_available": true
}
```

#### Información de Versión

```http
GET /
```

**Respuesta**
```json
{
  "name": "MoodBot API",
  "version": "2.0.0",
  "model": "Logistic Regression + Gemini AI",
  "accuracy": "92.93%",
  "features": [
    "ML Classification",
    "Empathetic Responses",
    "Resource Recommendations"
  ]
}
```

#### Predecir Emoción

```http
POST /predict
Content-Type: application/json
```

**Cuerpo de la Solicitud**
```json
{
  "message": "Me siento muy triste y sin esperanza"
}
```

**Respuesta**
```json
{
  "success": true,
  "prediction": {
    "label": "Depresion",
    "confidence": 0.8889
  },
  "response": "Lamento que estés pasando por un momento difícil. Tus sentimientos son válidos y mereces apoyo.\n\nLíneas de ayuda inmediata:\nTeléfono de la Esperanza: 717 003 717 (disponible 24/7)\nCruz Roja Responde: 900 107 917\nLínea de atención al suicidio: 024 (gratuita 24/7)\n\nRecursos adicionales:\nConsidera hablar con un profesional de salud mental\nMantén una rutina diaria estructurada\nBusca apoyo en familiares y amigos cercanos",
  "original_message": "Me siento muy triste y sin esperanza",
  "gemini_used": true
}
```

**Etiquetas de Clasificación**
- `Neutro`: Estado emocional neutral
- `Ansiedad`: Síntomas de ansiedad detectados
- `Depresion`: Indicadores de depresión presentes

**Respuesta de Error**
```json
{
  "success": false,
  "error": "Descripción del mensaje de error"
}
```

**Códigos de Estado**
- `200 OK`: Predicción exitosa
- `400 Bad Request`: Mensaje inválido o faltante
- `500 Internal Server Error`: Error del servidor o modelo

## Rendimiento del Modelo

### Métricas Generales

- **Algoritmo**: Regresión Logística
- **Precisión**: 92.93%
- **División Entrenamiento/Prueba**: 80/20
- **Validación cruzada**: K-fold (k=5)
- **Cantidad de Características**: 5,000 características TF-IDF
- **N-gramas**: (1, 2) - unigramas y bigramas

### Rendimiento por Clase

| Clase | Precisión | Recall | F1-Score | Soporte |
|-------|-----------|--------|----------|---------|
| Neutro | 0.94 | 0.93 | 0.93 | ~200 |
| Ansiedad | 0.91 | 0.92 | 0.91 | ~200 |
| Depresión | 0.93 | 0.94 | 0.93 | ~200 |
| **Promedio Macro** | **0.93** | **0.93** | **0.92** | **~600** |

### Características Principales por Clase

**Neutro**: okay, fine, normal, alright, good, well, calm, stable, content  
**Ansiedad**: worry, anxious, nervous, fear, panic, stress, overwhelm, restless  
**Depresión**: sad, hopeless, tired, empty, worthless, alone, depressed, lost

### Entrenamiento del Modelo

El modelo fue entrenado en un corpus de salud mental con el siguiente preprocesamiento:

1. **Limpieza de Texto**: Conversión a minúsculas, eliminación de caracteres especiales
2. **Tokenización**: Tokenización a nivel de palabra usando NLTK
3. **Eliminación de Stopwords**: Palabras vacías en inglés filtradas
4. **Stemming**: Aplicación de Porter Stemmer
5. **Vectorización**: TF-IDF con máximo de 5,000 características
6. **Balance de Clases**: Pesos de clase balanceados en Regresión Logística

## Estructura del Proyecto

### Repositorio Backend

```
moodbot-api/
├── app.py                      # Aplicación Flask principal
├── preprocessing.py            # Clase TextPreprocessor
├── train_model.py             # Script de entrenamiento del modelo
├── requirements.txt           # Dependencias Python
├── models/
│   ├── best_model.pkl        # Modelo de Regresión Logística entrenado
│   └── tfidf_vectorizer.pkl  # Vectorizador TF-IDF ajustado
└── README.md                  # Este archivo
```

### Repositorio Frontend

```
moodbot-frontend/
├── index.html                 # Estructura HTML principal
├── styles.css                 # Estilos y diseño responsive
├── script.js                  # Lógica del frontend y llamadas a API
└── README.md                  # Documentación del frontend
```

### Descripción de Archivos Clave

**app.py**: API REST de Flask con endpoints para verificaciones de estado y predicción de emociones. Integra modelo ML, Gemini AI y formato de recursos.

**preprocessing.py**: Contiene la clase `TextPreprocessor` con métodos para limpieza de texto, tokenización, eliminación de stopwords y stemming.

**train_model.py**: Script para entrenar el modelo de Regresión Logística con ajuste de hiperparámetros y validación cruzada.

**models/**: Archivos de modelo serializados usando joblib para despliegue en producción.

**index.html**: Estructura de interfaz de chat con mensaje de bienvenida, tarjetas de emociones y área de entrada.

**styles.css**: Estilos personalizados con esquema de color terracota/beige, diseño de cuadrícula responsive y transiciones suaves.

**script.js**: Maneja entrada del usuario, comunicación con API, renderizado de mensajes y funcionalidad de reinicio de chat.

## Despliegue

### Backend (Railway)

1. **Conectar Repositorio**
   - Vincular repositorio de GitHub a Railway
   - Seleccionar `moodbot-api` como directorio raíz

2. **Configurar Build**
   - Comando de Build: `pip install -r requirements.txt && python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('omw-1.4')"`
   - Comando de Inicio: `gunicorn app:app --bind 0.0.0.0:$PORT`

3. **Configurar Variables de Entorno**
   - `GEMINI_API_KEY`: Tu API key de Google Gemini
   - `PORT`: Configurado automáticamente por Railway

4. **Desplegar**
   - Despliegue automático al hacer push a rama `main`
   - Tiempo de build: ~2-3 minutos

### Frontend (Vercel)

1. **Conectar Repositorio**
   - Vincular repositorio de GitHub a Vercel
   - Framework: Ninguno (sitio estático)

2. **Configurar Build**
   - Comando de Build: (dejar vacío)
   - Directorio de Salida: `.`
   - Directorio Raíz: `./`

3. **Desplegar**
   - Despliegue automático al hacer push a rama `main`
   - Tiempo de despliegue: ~30-60 segundos

### Desarrollo Local

**Backend**
```bash
cd moodbot-api
export GEMINI_API_KEY='tu_api_key'
python app.py
# La API se ejecuta en http://localhost:5000
```

**Frontend**
```bash
cd moodbot-frontend
# Actualizar API_URL en script.js a http://localhost:5000
# Abrir index.html en navegador o usar live server
```

## Ejemplos de Uso

### Ejemplos con cURL

**Predicción Básica**
```bash
curl -X POST https://moodbot-production.up.railway.app/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "Me siento bien hoy"}'
```

**Detección de Depresión**
```bash
curl -X POST https://moodbot-production.up.railway.app/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "Me siento muy triste y sin esperanza"}'
```

**Detección de Ansiedad**
```bash
curl -X POST https://moodbot-production.up.railway.app/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "Tengo mucha ansiedad y no puedo dormir"}'
```

### Ejemplo en Python

```python
import requests

API_URL = "https://moodbot-production.up.railway.app/predict"

def analizar_emocion(mensaje):
    respuesta = requests.post(
        API_URL,
        json={"message": mensaje},
        headers={"Content-Type": "application/json"}
    )
    return respuesta.json()

# Ejemplo de uso
resultado = analizar_emocion("Me siento preocupado por el futuro")
print(f"Clasificación: {resultado['prediction']['label']}")
print(f"Confianza: {resultado['prediction']['confidence']:.2%}")
print(f"Respuesta: {resultado['response']}")
```

### Ejemplo en JavaScript

```javascript
const API_URL = 'https://moodbot-production.up.railway.app/predict';

async function analizarEmocion(mensaje) {
  try {
    const respuesta = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: mensaje }),
    });
    
    const datos = await respuesta.json();
    return datos;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}

// Ejemplo de uso
analizarEmocion('Hoy me siento ansioso')
  .then(resultado => {
    console.log('Clasificación:', resultado.prediction.label);
    console.log('Confianza:', resultado.prediction.confidence);
    console.log('Respuesta:', resultado.response);
  });
```

## Desarrollo

### Prerequisitos para Desarrollo

- Python 3.11+
- Node.js (para herramientas de frontend, opcional)
- VS Code o IDE preferido
- Git
- Postman o similar para pruebas de API

### Configurar Entorno de Desarrollo

1. **Fork y clonar repositorios**
   ```bash
   git clone https://github.com/TU_USUARIO/MoodBot.git
   git clone https://github.com/TU_USUARIO/moodbot-frontend.git
   ```

2. **Crear rama de característica**
   ```bash
   git checkout -b feature/nombre-de-tu-caracteristica
   ```

3. **Realizar cambios y probar localmente**

4. **Commit con mensajes descriptivos**
   ```bash
   git commit -m "feat: Añadir descripción de característica"
   ```

5. **Push y crear pull request**
   ```bash
   git push origin feature/nombre-de-tu-caracteristica
   ```

### Guías de Estilo de Código

**Python (Backend)**
- Seguir guía de estilo PEP 8
- Usar type hints donde sea aplicable
- Documentar funciones con docstrings
- Longitud máxima de línea: 100 caracteres

**JavaScript (Frontend)**
- Usar características ES6+
- Preferir `const` y `let` sobre `var`
- Usar funciones flecha para callbacks
- Documentar funciones complejas con comentarios JSDoc

**CSS**
- Usar convención de nomenclatura BEM donde sea aplicable
- Diseño responsive mobile-first
- Agrupar propiedades relacionadas
- Comentar selectores complejos

### Convención de Mensajes de Commit

- `feat:` Nueva característica
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `style:` Cambios de estilo de código (formato, etc.)
- `refactor:` Refactorización de código
- `test:` Añadir o actualizar pruebas
- `chore:` Tareas de mantenimiento

## Pruebas

### Pruebas Manuales

**Endpoints del Backend**
```bash
# Probar endpoint de estado
curl http://localhost:5000/health

# Probar predicción con varias entradas
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "mensaje de prueba"}'
```

**Frontend**
- Abrir consola de DevTools del navegador
- Probar funcionalidad de chat manualmente
- Verificar diseño responsive en diferentes tamaños de viewport
- Probar funcionalidad de click-to-reset
- Verificar renderizado de saltos de línea en respuestas

### Casos de Prueba

**Pruebas de Clasificación**

Probar el modelo con varios estados emocionales:

1. **Expresiones Neutrales**
   - "Hoy me siento bien"
   - "Todo está normal"
   - "Estoy tranquilo"

2. **Indicadores de Ansiedad**
   - "Me siento muy nervioso"
   - "Tengo mucha ansiedad"
   - "Estoy preocupado constantemente"

3. **Indicadores de Depresión**
   - "Me siento muy triste"
   - "No tengo esperanza"
   - "Me siento solo y vacío"

**Casos Extremos**
- Mensaje vacío
- Mensajes muy largos (>1000 caracteres)
- Caracteres especiales y emojis
- Mensajes en inglés (debería procesarse igual)
- Declaraciones no emocionales

### Pruebas de Rendimiento

Monitorear tiempos de respuesta de la API:
```bash
time curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "prueba"}'
```

Tiempos de respuesta esperados:
- Desarrollo local: <500ms
- Producción (Railway): <1500ms

## Contribuir

Las contribuciones son bienvenidas. Por favor, sigue estas pautas:

### Cómo Contribuir

1. **Fork del repositorio**
2. **Crear una rama de característica** (`git checkout -b feature/CaracteristicaAsombrosa`)
3. **Realizar tus cambios**
4. **Probar exhaustivamente**
5. **Commit de tus cambios** (`git commit -m 'feat: Añadir CaracteristicaAsombrosa'`)
6. **Push a la rama** (`git push origin feature/CaracteristicaAsombrosa`)
7. **Abrir un Pull Request**

### Pautas para Pull Requests

- Proporcionar descripción clara de los cambios
- Referenciar issues relacionados si aplica
- Incluir resultados de pruebas
- Actualizar documentación si es necesario
- Seguir el estilo de código existente
- Asegurar que todas las pruebas pasen

### Reportar Issues

Al reportar issues, por favor incluye:

- Descripción clara del problema
- Pasos para reproducir
- Comportamiento esperado vs real
- Detalles del entorno (SO, versión de Python, etc.)
- Mensajes de error o capturas de pantalla si aplica

### Solicitudes de Características

Para solicitudes de características, por favor describe:

- Caso de uso y motivación
- Solución propuesta o enfoque de implementación
- Impacto potencial en funcionalidad existente

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver abajo para detalles:

```
Licencia MIT

Copyright (c) 2025 Angie Díaz

Por la presente se concede permiso, libre de cargos, a cualquier persona que obtenga una copia
de este software y de los archivos de documentación asociados (el "Software"), para utilizar
el Software sin restricción, incluyendo sin limitación los derechos de usar, copiar, modificar,
fusionar, publicar, distribuir, sublicenciar, y/o vender copias del Software, y para permitir
a las personas a las que se les proporcione el Software hacer lo mismo, sujeto a las siguientes
condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o
porciones sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA,
INCLUYENDO PERO NO LIMITADO A GARANTÍAS DE COMERCIALIZACIÓN, IDONEIDAD PARA UN PROPÓSITO
PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DEL COPYRIGHT SERÁN
RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN
DE CONTRATO, AGRAVIO O CUALQUIER OTRO MOTIVO, QUE SURJA DE O EN CONEXIÓN CON EL SOFTWARE O
EL USO U OTROS TRATOS EN EL SOFTWARE.
```

## Consideraciones Éticas

### Disclaimers Importantes

**Esta es una herramienta de apoyo, no un dispositivo médico**
- MoodBot no proporciona diagnósticos médicos
- No es un sustituto de atención profesional de salud mental
- Los usuarios que experimenten una crisis deben contactar servicios de emergencia o líneas de crisis inmediatamente

### Privacidad y Datos

- No se almacenan ni registran datos de usuario
- Las conversaciones no se persisten
- API sin estado - sin seguimiento de usuarios
- No se requiere información personal
- No se usan cookies ni almacenamiento local

### Limitaciones

- Limitado a tres categorías emocionales
- Puede no detectar sarcasmo o ironía
- Optimizado para español pero procesa texto traducido
- Los puntajes de confianza son estimaciones, no certezas
- No puede detectar severidad o urgencia más allá de la clasificación de categoría

### Recursos de Crisis

Si tú o alguien que conoces está en crisis, por favor contacta:

**España**
- Teléfono de la Esperanza: 717 003 717 (24/7)
- Línea de atención al suicidio: 024 (gratuita, 24/7)
- Cruz Roja Responde: 900 107 917

**Internacional**
- International Association for Suicide Prevention: https://www.iasp.info/resources/Crisis_Centres/

## Agradecimientos

- **scikit-learn**: Framework de machine learning
- **NLTK**: Herramientas de procesamiento de lenguaje natural
- **Google Gemini**: Generación de respuestas IA
- **Flask**: Framework web
- **Railway y Vercel**: Plataformas de despliegue
- **Comunidad open source**: Varias bibliotecas y herramientas

## Hoja de Ruta

### Versión 2.1 (Planificada)

- Persistencia de historial de conversaciones
- Exportar conversación como PDF
- Categorías emocionales adicionales (Ira, Miedo, Alegría)
- Soporte multilingüe (catalán, euskera, gallego)

### Versión 3.0 (Futuro)

- Modelos de deep learning (BERT, transformers)
- Detección de intensidad emocional
- Análisis temporal (seguimiento del estado de ánimo a lo largo del tiempo)
- Aplicación móvil (React Native)
- Dashboard profesional para terapeutas

## Contacto

**Autora**: Angie Díaz

**GitHub**: [@AngieDiaz25](https://github.com/AngieDiaz25)

**Enlaces del Proyecto**:
- Backend: [https://github.com/AngieDiaz25/MoodBot](https://github.com/AngieDiaz25/MoodBot)
- Frontend: [https://github.com/AngieDiaz25/moodbot-frontend](https://github.com/AngieDiaz25/moodbot-frontend)

**Demo en Vivo**:
- API: [https://moodbot-production.up.railway.app](https://moodbot-production.up.railway.app)
- Interfaz Web: [Tu URL de Vercel]

---

**Última Actualización**: 28 de Noviembre de 2025  
**Versión**: 2.0.0  
**Estado**: Producción
