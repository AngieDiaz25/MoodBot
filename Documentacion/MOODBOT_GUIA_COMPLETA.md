# 🤖 MOODBOT - GUÍA COMPLETA DEL PROYECTO

**Fecha:** 18 de Noviembre, 2025  
**Estado:** ✅ API funcionando correctamente  
**Accuracy del modelo:** 92.93%

---

## 📊 RESUMEN DEL PROYECTO

MoodBot es un chatbot de clasificación de estados emocionales usando Machine Learning.

**Tecnologías:**
- Python 3.11
- Flask (API REST)
- scikit-learn (Logistic Regression)
- NLTK (Procesamiento de lenguaje natural)
- TF-IDF Vectorización

**Clasificaciones:**
- 😐 Neutro
- 😰 Ansiedad
- 😢 Depresión

---

## 📁 ESTRUCTURA DEL PROYECTO

```
/Users/angiediaz/Desktop/Proyecto ML/
│
├── API/                              # ⭐ CARPETA PRINCIPAL DE LA API
│   ├── app.py                        # Servidor Flask
│   ├── preprocessing.py              # Preprocesamiento de texto
│   ├── requirements.txt              # Dependencias Python
│   ├── venv/                         # Entorno virtual
│   │   └── (librerías instaladas)
│   └── models/                       # Modelos entrenados
│       ├── best_model.pkl            # Logistic Regression
│       └── tfidf_vectorizer.pkl      # Vectorizador TF-IDF
│
├── Models/                           # Modelos originales (backup)
│   ├── best_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── model_metadata.pkl
│
├── Data/                             # Datasets procesados
│   ├── moodbot_processed_train.csv
│   ├── moodbot_processed_test.csv
│   └── moodbot_processed_val.csv
│
├── Results/                          # Resultados del entrenamiento
├── EDA_Results/                      # Análisis exploratorio
└── Entrenar_Modelos.ipynb            # Notebook de entrenamiento
```

---

## 🚀 CÓMO INICIAR LA API

### **Método 1: Comandos completos**

```bash
# 1. Abrir Terminal (Cmd + Espacio → "Terminal")

# 2. Navegar a la carpeta API
cd "/Users/angiediaz/Desktop/Proyecto ML/API"

# 3. Activar entorno virtual
source venv/bin/activate

# Deberías ver (venv) al inicio de la línea

# 4. Ejecutar el servidor
python app.py
```

### **Método 2: Script rápido (copiar y pegar todo)**

```bash
cd "/Users/angiediaz/Desktop/Proyecto ML/API" && source venv/bin/activate && python app.py
```

---

## ✅ VERIFICAR QUE FUNCIONA

Deberías ver esto en la terminal:

```
==================================================
MOODBOT API - INICIANDO
==================================================
Modelo cargado
Vectorizador cargado
Preprocessor inicializado
Modelos cargados correctamente
Servidor iniciado en http://127.0.0.1:5000
 * Serving Flask app 'app'
 * Debug mode: on
```

**¡El servidor está corriendo!** No cierres esta terminal.

---

## 🧪 PROBAR LA API

Abre **OTRA terminal** y ejecuta estos comandos:

### **1. Health Check**
```bash
curl http://localhost:5000/health
```

**Respuesta esperada:**
```json
{
  "models_loaded": true,
  "status": "healthy"
}
```

### **2. Predicción - Ansiedad**
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "I feel so anxious and worried today"}'
```

**Respuesta esperada:**
```json
{
  "success": true,
  "prediction": {
    "label": "Ansiedad",
    "confidence": 0.9843
  },
  "response": "La ansiedad puede ser abrumadora...",
  "original_message": "I feel so anxious and worried today"
}
```

### **3. Predicción - Depresión**
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "I feel sad and hopeless"}'
```

### **4. Predicción - Neutro**
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the weather like today?"}'
```

---

## 📡 ENDPOINTS DISPONIBLES

### **GET /**
Información general de la API

**URL:** `http://localhost:5000/`

**Respuesta:**
```json
{
  "name": "MoodBot API",
  "version": "1.0.0",
  "model": "Logistic Regression",
  "accuracy": "92.93%"
}
```

---

### **GET /health**
Verificar estado de la API

**URL:** `http://localhost:5000/health`

**Respuesta:**
```json
{
  "status": "healthy",
  "models_loaded": true
}
```

---

### **POST /predict**
Clasificar un mensaje

**URL:** `http://localhost:5000/predict`

**Headers:**
```
Content-Type: application/json
```

**Body:**
```json
{
  "message": "Tu mensaje aquí"
}
```

**Respuesta:**
```json
{
  "success": true,
  "prediction": {
    "label": "Ansiedad|Depresion|Neutro",
    "confidence": 0.9186
  },
  "response": "Respuesta empática del bot",
  "original_message": "Tu mensaje original"
}
```

---

## 🛑 DETENER EL SERVIDOR

En la terminal donde está corriendo el servidor:

**Presiona:** `Ctrl + C`

---

## 🔧 TROUBLESHOOTING

### **Problema: "command not found: python"**

**Solución:** Usa `python3` en lugar de `python`

```bash
python3 app.py
```

---

### **Problema: "No module named 'flask'"**

**Solución:** El entorno virtual no está activado

```bash
source venv/bin/activate
python app.py
```

---

### **Problema: "Error loading models"**

**Solución:** Los modelos no están en la carpeta correcta

```bash
# Verificar que existan
ls -la models/

# Si no existen, copiarlos
cp ../Models/best_model.pkl models/
cp ../Models/tfidf_vectorizer.pkl models/
```

---

### **Problema: "Port 5000 already in use"**

**Solución:** Ya hay un servidor corriendo

**Opción 1:** Encuentra y detén el proceso
```bash
lsof -ti:5000 | xargs kill -9
```

**Opción 2:** Usa otro puerto (edita app.py línea 68)
```python
app.run(host='0.0.0.0', port=5001, debug=True)
```

---

### **Problema: "Resource punkt_tab not found"**

**Solución:** Descargar recursos de NLTK

```bash
source venv/bin/activate
python -c "import nltk; nltk.download('punkt_tab')"
python app.py
```

---

## 📊 MÉTRICAS DEL MODELO

### **Accuracy General: 92.93%**

| Clase | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| Neutro | 100% | 100% | 100% |
| Ansiedad | 88.16% | 90.97% | 89.55% |
| Depresión | 90.69% | 87.81% | 89.23% |

---

## 🔄 REGENERAR LOS MODELOS (si es necesario)

Si necesitas volver a entrenar los modelos:

### **Opción 1: Desde VS Code**

1. Abre `Entrenar_Modelos.ipynb` en VS Code
2. Selecciona el kernel: **Python (MoodBot venv)**
3. Ejecuta: **Run All**
4. Espera a que termine
5. Copia los nuevos modelos:

```bash
cd "/Users/angiediaz/Desktop/Proyecto ML/API"
rm models/*.pkl
cp ../Models/best_model.pkl models/
cp ../Models/tfidf_vectorizer.pkl models/
```

---

## 📦 DEPENDENCIAS INSTALADAS

Versiones actuales en el entorno virtual:

```
Flask==3.1.0
flask-cors==5.0.0
scikit-learn==1.7.2
nltk==3.9.1
numpy==2.3.5
pandas==2.3.3
joblib==1.4.2
```

---

## 🚀 PRÓXIMOS PASOS

### **1. Deployment (hacer la API pública)**

**Opciones:**
- Render (recomendado - gratis)
- Railway
- Heroku

**Tiempo estimado:** 30-45 minutos

---

### **2. Crear Frontend**

**Tecnologías sugeridas:**
- React + Next.js
- Vercel para hosting

**Componentes necesarios:**
- Interfaz de chat
- Input para mensajes
- Display de respuestas
- Indicador de estado emocional

**Tiempo estimado:** 1-2 horas

---

### **3. Mejoras al modelo**

**Ideas:**
- Agregar más categorías emocionales
- Entrenar con más datos
- Implementar modelo más avanzado (BERT, transformers)
- Agregar análisis de sentimiento continuo

---

## 📝 NOTAS IMPORTANTES

### **✅ Lo que está FUNCIONANDO:**
- API REST completa
- Modelo ML integrado (92.93% accuracy)
- Preprocesamiento NLP automático
- Clasificación en 3 categorías
- Respuestas empáticas personalizadas

### **⏳ Lo que FALTA (opcional):**
- Deployment en servidor público
- Frontend (interfaz de usuario)
- Base de datos para guardar conversaciones
- Sistema de logs
- Tests automatizados

---

## 🔒 SEGURIDAD

**Para producción (cuando despliegues):**

1. ✅ **Deshabilitar debug mode**
   ```python
   app.run(host='0.0.0.0', port=5000, debug=False)
   ```

2. ✅ **Usar servidor WSGI (gunicorn)**
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

3. ✅ **Configurar CORS apropiadamente**
   - Solo permitir dominios específicos
   - No usar `*` en producción

4. ✅ **Agregar rate limiting**
   - Evitar abuso de la API
   - Usar Flask-Limiter

---

## 📞 CONTACTO Y RECURSOS

**Proyecto:** MoodBot - Clasificador de Estados Emocionales  
**Autor:** Angie Díaz  
**Fecha:** Noviembre 2025

**Recursos útiles:**
- Flask docs: https://flask.palletsprojects.com/
- scikit-learn docs: https://scikit-learn.org/
- NLTK docs: https://www.nltk.org/

---

## ✨ ¡FELICIDADES!

Has completado exitosamente:
- ✅ Preprocesamiento de datos
- ✅ Entrenamiento de modelos ML
- ✅ Creación de API REST
- ✅ Integración de NLP
- ✅ Sistema funcionando end-to-end

**¡Excelente trabajo!** 🎉

---

**Última actualización:** 18 de Noviembre, 2025  
**Estado del proyecto:** ✅ API funcionando localmente  
**Próximo hito:** Deployment en servidor público
