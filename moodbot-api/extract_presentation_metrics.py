#!/usr/bin/env python3
import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print("="*70)
print("EXTRACCIÓN DE MÉTRICAS PARA PRESENTACIÓN MOODBOT")
print("="*70)

label_mapping = {0: "Neutro", 1: "Ansiedad", 2: "Depresión"}

print("\n1. Cargando modelos...")
model = joblib.load('models/best_model.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')
print("   ✓ Modelos cargados")

print("\n2. Cargando datos de test...")
try:
    test = pd.read_csv('../Data/moodbot_processed_test.csv')
except:
    test = pd.read_csv('../Data/moodbot_processed_train.csv').sample(frac=0.2, random_state=42)
print(f"   ✓ Test: {len(test)} muestras")

X_test = test['cleaned_text']
y_test = test['label']

print("\n" + "="*70)
print("MÉTRICAS")
print("="*70)

X_test_tfidf = vectorizer.transform(X_test)
y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nACCURACY: {accuracy*100:.2f}%")

target_names = ["Neutro", "Ansiedad", "Depresión"]
print("\n" + classification_report(y_test, y_pred, target_names=target_names))

cm = confusion_matrix(y_test, y_pred)
print("\nMATRIZ DE CONFUSIÓN:")
print("              " + "  ".join([f"{n:>10s}" for n in target_names]))
for i, label in enumerate(target_names):
    print(f"Real {label:12s}" + "".join([f"  {cm[i][j]:>10d}" for j in range(3)]))

print("\nTOP 10 FEATURES POR CLASE:")
feature_names = vectorizer.get_feature_names_out()
for i, class_name in enumerate(target_names):
    print(f"\n{class_name}:")
    top_idx = np.argsort(model.coef_[i])[-10:][::-1]
    for rank, idx in enumerate(top_idx, 1):
        print(f"  {rank:2d}. {feature_names[idx]}")

print("\n✓ Completado")
