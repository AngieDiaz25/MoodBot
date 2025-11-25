from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
from preprocessing import TextPreprocessor
from deep_translator import GoogleTranslator

app = Flask(__name__)
CORS(app)

model = None
vectorizer = None
preprocessor = None
label_mapping = {0: "Neutro", 1: "Ansiedad", 2: "Depresion"}

RESPONSES = {
    "Neutro": ["Entiendo. Hay algo mas que quieras compartir?"],
    "Ansiedad": ["La ansiedad puede ser abrumadora, pero estas dando un paso importante."],
    "Depresion": ["Lamento que estes pasando por un momento dificil. Tus sentimientos son validos."]
}


translator_es_en = GoogleTranslator(source='es', target='en')
translator_en_es = GoogleTranslator(source='en', target='es')

def load_models():
    global model, vectorizer, preprocessor
    try:
        model_path = os.path.join('models', 'best_model.pkl')
        vectorizer_path = os.path.join('models', 'tfidf_vectorizer.pkl')
        
        model = joblib.load(model_path)
        print("Modelo cargado")
        
        vectorizer = joblib.load(vectorizer_path)
        print("Vectorizador cargado")
        
        preprocessor = TextPreprocessor()
        print("Preprocessor inicializado")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "models_loaded": model is not None}), 200

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
            response_es = translator_en_es.translate(RESPONSES["Neutro"][0])
            return jsonify({
                "success": True,
                "prediction": {"label": "Neutro", "confidence": 1.0},
                "response": response_es
            }), 200
        
        # Clasificar
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

        # Si tiene palabras positivas SIN negaciones, ajustar a Neutro si la confianza es baja
        if has_positive and not has_negative and confidence < 0.85 and label != "Neutro":
            print(f"⚙️  Ajustando predicción: palabras positivas detectadas")
            label = "Neutro"
            confidence = 0.75

        print(f"🔵 Predicción final: {label} ({confidence:.2%})")

        # Traducir respuesta a español
        try:
            response_es = translator_en_es.translate(RESPONSES[label][0])
        except:
            response_es = RESPONSES[label][0]
        
        return jsonify({
            "success": True,
            "prediction": {"label": label, "confidence": round(confidence, 4)},
            "response": response_es,
            "original_message": message
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({"name": "MoodBot API", "version": "1.0.0", "model": "Logistic Regression", "accuracy": "92.93%"}), 200

print("=" * 50)
print("MOODBOT API - INICIANDO")
print("=" * 50)
load_models()

if __name__ == '__main__':
    print("="*50)
    print("MOODBOT API - INICIANDO")
    print("="*50)
    if load_models():
        print("Modelos cargados correctamente")
        print("Servidor iniciado en http://127.0.0.1:5000")
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        print("No se pudieron cargar los modelos")
