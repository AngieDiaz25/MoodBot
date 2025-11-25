"""
MoodBot API - Flask Server
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os
from preprocessing import TextPreprocessor

app = Flask(__name__)
CORS(app)

model = None
vectorizer = None
preprocessor = None
label_mapping = {0: "Neutro", 1: "Ansiedad", 2: "Depresión"}

RESPONSES = {
    "Neutro": ["Entiendo. ¿Hay algo más que quieras compartir?"],
    "Ansiedad": ["La ansiedad puede ser abrumadora, pero estás dando un 
paso importante al hablar de ello."],
    "Depresión": ["Lamento que estés pasando por un momento difícil. Tus 
sentimientos son válidos."]
}

def load_models():
    global model, vectorizer, preprocessor
    try:
        model_path = os.path.join('models', 'best_model.pkl')
        vectorizer_path = os.path.join('models', 'tfidf_vectorizer.pkl')
        
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        print(f"✓ Modelo cargado")
        
        with open(vectorizer_path, 'rb') as f:
            vectorizer = pickle.load(f)
        print(f"✓ Vectorizador cargado")
        
        preprocessor = TextPreprocessor()
        print("✓ Preprocessor inicializado")
        return True
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "models_loaded": model is not None
    }), 200

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or vectorizer is None:
        return jsonify({"success": False, "error": "Models not loaded"}), 
500
    
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"success": False, "error": "Missing 
'message'"}), 400
        
        message = data['message']
        if not message.strip():
            return jsonify({"success": False, "error": "Empty message"}), 
400
        
        preprocessed = preprocessor.preprocess(message)
        if not preprocessed.strip():
            return jsonify({
                "success": True,
                "prediction": {"label": "Neutro", "confidence": 1.0},
                "response": RESPONSES["Neutro"][0]
            }), 200
        
        vectorized = vectorizer.transform([preprocessed])
        prediction = model.predict(vectorized)[0]
        probabilities = model.predict_proba(vectorized)[0]
        
        label = label_mapping[prediction]
        confidence = float(probabilities[prediction])
        
        return jsonify({
            "success": True,
            "prediction": {
                "label": label,
                "confidence": round(confidence, 4)
            },
            "response": RESPONSES[label][0],
            "original_message": message
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "name": "MoodBot API",
        "version": "1.0.0",
        "model": "Logistic Regression",
        "accuracy": "92.93%"
    }), 200

if __name__ == '__main__':
    print("="*50)
    print("MOODBOT API - INICIANDO")
    print("="*50)
    
    if load_models():
        print("✓ Modelos cargados")
        print("🚀 Servidor iniciado en http://127.0.0.1:5000")
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        print("❌ No se pudieron cargar los modelos")

"""
MoodBot API - Flask Server
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os
from preprocessing import TextPreprocessor

app = Flask(__name__)
CORS(app)

model = None
vectorizer = None
preprocessor = None
label_mapping = {0: "Neutro", 1: "Ansiedad", 2: "Depresión"}

RESPONSES = {
    "Neutro": ["Entiendo. ¿Hay algo más que quieras compartir?"],
    "Ansiedad": ["La ansiedad puede ser abrumadora, pero estás dando un 
paso importante al hablar de ello."],
    "Depresión": ["Lamento que estés pasando por un momento difícil. Tus 
sentimientos son válidos."]
}

def load_models():
    global model, vectorizer, preprocessor
    try:
        model_path = os.path.join('models', 'best_model.pkl')
        vectorizer_path = os.path.join('models', 'tfidf_vectorizer.pkl')
        
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        print(f"✓ Modelo cargado")
        
        with open(vectorizer_path, 'rb') as f:
            vectorizer = pickle.load(f)
        print(f"✓ Vectorizador cargado")
        
        preprocessor = TextPreprocessor()
        print("✓ Preprocessor inicializado")
        return True
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "models_loaded": model is not None
    }), 200

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or vectorizer is None:
        return jsonify({"success": False, "error": "Models not loaded"}), 
500
    
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"success": False, "error": "Missing 
'message'"}), 400
        
        message = data['message']
        if not message.strip():
            return jsonify({"success": False, "error": "Empty message"}), 
400
        
        preprocessed = preprocessor.preprocess(message)
        if not preprocessed.strip():
            return jsonify({
                "success": True,
                "prediction": {"label": "Neutro", "confidence": 1.0},
                "response": RESPONSES["Neutro"][0]
            }), 200
        
        vectorized = vectorizer.transform([preprocessed])
        prediction = model.predict(vectorized)[0]
        probabilities = model.predict_proba(vectorized)[0]
        
        label = label_mapping[prediction]
        confidence = float(probabilities[prediction])
        
        return jsonify({
            "success": True,
            "prediction": {
                "label": label,
                "confidence": round(confidence, 4)
            },
            "response": RESPONSES[label][0],
            "original_message": message
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "name": "MoodBot API",
        "version": "1.0.0",
        "model": "Logistic Regression",
        "accuracy": "92.93%"
    }), 200

if __name__ == '__main__':
    print("="*50)
    print("MOODBOT API - INICIANDO")
    print("="*50)
    
    if load_models():
        print("✓ Modelos cargados")
        print("🚀 Servidor iniciado en http://127.0.0.1:5000")
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        print("❌ No se pudieron cargar los modelos")



