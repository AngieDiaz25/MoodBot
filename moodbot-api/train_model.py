import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

print("="*60)
print("ENTRENANDO MODELO MOODBOT")
print("="*60)

# 1. Cargar datos
print("\n1. Cargando datos...")
train = pd.read_csv('../Data/moodbot_processed_train.csv')
print(f"   Train: {len(train)} muestras")

# 2. Preparar X e y
print("\n2. Preparando datos...")
X_train = train['cleaned_text']  # Ajusta el nombre de la columna si es diferente
y_train = train['label']

print(f"   Distribución de clases:")
print(y_train.value_counts())

# 3. Vectorización TF-IDF
print("\n3. Creando vectorizador TF-IDF...")
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
print(f"   Shape: {X_train_tfidf.shape}")

# 4. Entrenar modelo
print("\n4. Entrenando Logistic Regression...")
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_tfidf, y_train)
print("   ✓ Modelo entrenado")

# 5. Guardar modelos
print("\n5. Guardando modelos...")
with open('../Models/best_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("   ✓ best_model.pkl guardado")

with open('../Models/tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
print("   ✓ tfidf_vectorizer.pkl guardado")

print("\n" + "="*60)
print("✅ ENTRENAMIENTO COMPLETADO")
print("="*60)
