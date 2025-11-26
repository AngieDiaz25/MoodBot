# ⚡ MOODBOT - COMANDOS RÁPIDOS

## 🚀 INICIAR SERVIDOR

```bash
cd "/Users/angiediaz/Desktop/Proyecto ML/API"
source venv/bin/activate
python app.py
```

---

## 🧪 PROBAR API (en otra terminal)

### Health Check
```bash
curl http://localhost:5000/health
```

### Predicción
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "I feel anxious"}'
```

---

## 🛑 DETENER SERVIDOR

```
Ctrl + C
```

---

## 🔄 REGENERAR MODELOS

1. Abrir `Entrenar_Modelos.ipynb` en VS Code
2. Seleccionar kernel: Python (MoodBot venv)
3. Run All
4. Copiar modelos:

```bash
cd "/Users/angiediaz/Desktop/Proyecto ML/API"
rm models/*.pkl
cp ../Models/*.pkl models/
```

---

## 🐛 SOLUCIONAR PROBLEMAS

### Entorno virtual no activo
```bash
source venv/bin/activate
```

### Puerto ocupado
```bash
lsof -ti:5000 | xargs kill -9
```

### NLTK faltante
```bash
python -c "import nltk; nltk.download('punkt_tab')"
```

---

## 📊 ENDPOINTS

- `GET /` - Info
- `GET /health` - Status
- `POST /predict` - Clasificar

---

**Servidor:** http://localhost:5000  
**Documentación completa:** MOODBOT_GUIA_COMPLETA.md
