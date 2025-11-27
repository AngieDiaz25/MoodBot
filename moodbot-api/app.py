from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
from preprocessing import TextPreprocessor
from deep_translator import GoogleTranslator
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

model = None
vectorizer = None
preprocessor = None
gemini_model = None
label_mapping = {0: "Neutro", 1: "Ansiedad", 2: "Depresion"}

# Recursos de ayuda por categoría
RESOURCES = {
    "Depresion": {
        "lineas_ayuda": [
            "📞 Teléfono de la Esperanza: 717 003 717 (disponible 24/7)",
            "📞 Cruz Roja Responde: 900 107 917",
            "📞 Línea de atención al suicidio: 024 (gratuita 24/7)"
        ],
        "recursos": [
            "💡 Considera hablar con un profesional de salud mental",
            "💡 Mantén una rutina diaria estructurada",
            "💡 Busca apoyo en familiares y amigos cercanos"
        ]
    },
    "Ansiedad": {
        "tecnicas": [
            "🧘 Respiración 4-7-8: Inhala 4 seg, mantén 7 seg, exhala 8 seg",
            "🧘 Técnica de grounding: Nombra 5 cosas que ves, 4 que tocas, 3 que oyes",
            "🧘 Meditación mindfulness de 5 minutos"
        ],
        "recursos": [
            "💡 Directorio de psicólogos: colegiodepsicologos.es",
            "💡 Apps recomendadas: Calm, Headspace para meditación",
            "💡 Considera terapia cognitivo-conductual (TCC)"
        ]
    },
    "Neutro": {
        "prevencion": [
            "✨ Mantén hábitos saludables: sueño regular, ejercicio, alimentación balanceada",
            "✨ Practica autocuidado y establece límites saludables",
            "✨ Cultiva relaciones sociales positivas"
        ]
    }
}

# Fallback responses si Gemini no está disponible
FALLBACK_RESPONSES = {
    "Neutro": "Entiendo. ¿Hay algo más que quieras compartir?",
    "Ansiedad": "La ansiedad puede ser abrumadora, pero estás dando un paso importante al hablar de ello.",
    "Depresion": "Lamento que estés pasando por un momento difícil. Tus sentimientos son válidos y mereces apoyo."
}

translator_es_en = GoogleTranslator(source='es', target='en')
translator_en_es = GoogleTranslator(source='en', target='es')

def load_models():
    global model, vectorizer, preprocessor, gemini_model
    try:
        model_path = os.path.join('models', 'best_model.pkl')
        vectorizer_path = os.path.join('models', 'tfidf_vectorizer.pkl')
        
        model = joblib.load(model_path)
        print("✓ Modelo cargado")
        
        vectorizer = joblib.load(vectorizer_path)
        print("✓ Vectorizador cargado")
        
        preprocessor = TextPreprocessor()
        print("✓ Preprocessor inicializado")
        
        # Configurar Gemini
        api_key = os.getenv('GEMINI_API_KEY')
        if api_key:
            genai.configure(api_key=api_key)
            gemini_model = genai.GenerativeModel('gemini-pro')
            print("✓ Gemini configurado")
        else:
            print("⚠️  GEMINI_API_KEY no encontrada, usando respuestas fallback")
        
        return True
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

def generate_empathetic_response(message, classification, confidence):
    """
    Genera una respuesta empática usando Gemini basada en la clasificación ML
    """
    if not gemini_model:
        return FALLBACK_RESPONSES[classification]
    
    try:
        prompt = f"""Eres un asistente de apoyo emocional empático y profesional. 
        
Un usuario ha compartido: "{message}"

Nuestro sistema de análisis ha detectado que el estado emocional predominante es: {classification} (confianza: {confidence:.0%})

Genera una respuesta que:
1. Sea empática y validante
2. Reconozca sus sentimientos sin juzgar
3. Sea breve (2-3 oraciones máximo)
4. Use un tono cálido pero profesional
5. No hagas diagnósticos ni des consejos médicos específicos
6. Responde en español

Respuesta:"""

        response = gemini_model.generate_content(prompt)
        return response.text.strip()
        
    except Exception as e:
        print(f"⚠️  Error en Gemini: {str(e)}")
        return FALLBACK_RESPONSES[classification]

def format_resources(classification):
    """
    Formatea los recursos de ayuda según la clasificación
    """
    resources = RESOURCES.get(classification, {})
    formatted = []
    
    if "lineas_ayuda" in resources:
        formatted.append("\n🆘 Líneas de ayuda inmediata:")
        formatted.extend(resources["lineas_ayuda"])
    
    if "tecnicas" in resources:
        formatted.append("\n🧘 Técnicas que pueden ayudar:")
        formatted.extend(resources["tecnicas"])
    
    if "recursos" in resources:
        formatted.append("\n💡 Recursos adicionales:")
        formatted.extend(resources["recursos"])
    
    if "prevencion" in resources:
        formatted.append("\n✨ Recomendaciones para el bienestar:")
        formatted.extend(resources["prevencion"])
    
    return "\n".join(formatted) if formatted else ""

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy", 
        "models_loaded": model is not None,
        "gemini_available": gemini_model is not None
    }), 200

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or vectorizer is None:
        return jsonify({"success": False, "error": "Models not loaded"}), 500
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"success": False, "error": "Missing message"}), 400
        
        message = data['message']
        if not message.strip():
            return jsonify({"success": False, "error": "Empty message"}), 400
        
        # Traducir de español a inglés
        try:
            message_en = translator_es_en.translate(message[:4999])
            print(f"🔵 Original (ES): {message}")
            print(f"🔵 Traducido (EN): {message_en}")
        except:
            message_en = message
            print(f"⚠️  Translation failed, using original: {message}")
        
        # Preprocesar en inglés
        preprocessed = preprocessor.preprocess(message_en)
        print(f"🔵 Preprocesado: {preprocessed}")
        
        if not preprocessed.strip():
            response_text = generate_empathetic_response(message, "Neutro", 1.0)
            return jsonify({
                "success": True,
                "prediction": {"label": "Neutro", "confidence": 1.0},
                "response": response_text
            }), 200
        
        # Clasificar con ML
        vectorized = vectorizer.transform([preprocessed])
        prediction = model.predict(vectorized)[0]
        probabilities = model.predict_proba(vectorized)[0]

        label = label_mapping[prediction]
        confidence = float(probabilities[prediction])
        print(f"🔵 Predicción original: {label} ({confidence:.2%})")

        # Ajuste basado en palabras clave positivas/negativas
        positive_words = ['happy', 'great', 'wonderful', 'excited', 'joy', 'love', 'good', 'better', 'amazing']
        negative_words = ['not', 'never', 'can\'t', 'don\'t', 'won\'t', 'no', 'without']

        has_positive = any(word in preprocessed.lower() for word in positive_words)
        has_negative = any(word in preprocessed.lower() for word in negative_words)

        if has_positive and not has_negative and confidence < 0.85 and label != "Neutro":
            print(f"⚙️  Ajustando predicción: palabras positivas detectadas")
            label = "Neutro"
            confidence = 0.75

        print(f"🔵 Predicción final: {label} ({confidence:.2%})")

        # Generar respuesta empática con Gemini
        empathetic_response = generate_empathetic_response(message, label, confidence)
        
        # Agregar recursos de ayuda
        resources_text = format_resources(label)
        
        # Combinar respuesta empática + recursos
        full_response = empathetic_response
        if resources_text:
            full_response += f"\n{resources_text}"
        
        return jsonify({
            "success": True,
            "prediction": {"label": label, "confidence": round(confidence, 4)},
            "response": full_response,
            "original_message": message,
            "gemini_used": gemini_model is not None
        }), 200
        
    except Exception as e:
        print(f"✗ Error en predict: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "name": "MoodBot API", 
        "version": "2.0.0", 
        "model": "Logistic Regression + Gemini AI", 
        "accuracy": "92.93%",
        "features": ["ML Classification", "Empathetic Responses", "Resource Recommendations"]
    }), 200

print("=" * 50)
print("MOODBOT API v2.0 - INICIANDO")
print("=" * 50)
load_models()

if __name__ == '__main__':
    print("="*50)
    print("MOODBOT API v2.0 - INICIANDO")
    print("="*50)
    if load_models():
        print("✓ Modelos cargados correctamente")
        print("Servidor iniciado en http://127.0.0.1:5000")
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        print("✗ No se pudieron cargar los modelos")