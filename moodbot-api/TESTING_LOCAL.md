# 🧪 Guía de Testing Local - MoodBot Frontend

## 📋 Preparación

### Paso 1: Organizar los Archivos

Crea una carpeta para tu proyecto y descarga TODOS estos archivos ahí:

```
📁 moodbot-frontend/
├── index.html          ← Descarga
├── styles.css          ← Descarga
├── script.js           ← Descarga
├── vercel.json         ← Descarga
├── server.py           ← Descarga (opcional, para servidor fácil)
└── .gitignore          ← Renombra gitignore.txt a .gitignore
```

---

## 🚀 Opción 1: Servidor con Script Python (Más Fácil)

### Windows, Mac o Linux

```bash
# 1. Abre terminal/CMD en la carpeta del proyecto

# 2. Ejecuta el servidor
python server.py

# 3. El navegador se abrirá automáticamente en http://localhost:8000
# Si no se abre, abre manualmente esa URL
```

**Ventajas:**
- ✅ Se abre el navegador automáticamente
- ✅ Bonito mensaje de bienvenida
- ✅ CORS configurado correctamente

---

## 🚀 Opción 2: Servidor Python Simple

```bash
# En la carpeta del proyecto
python -m http.server 8000

# Luego abre tu navegador en:
# http://localhost:8000
```

---

## 🚀 Opción 3: Node.js (si tienes Node instalado)

```bash
# Instalar http-server globalmente (solo una vez)
npm install -g http-server

# Ejecutar servidor
http-server -p 8000

# Abrir: http://localhost:8000
```

---

## 🚀 Opción 4: Visual Studio Code

1. Instala la extensión **"Live Server"** de Ritwick Dey
2. Abre la carpeta del proyecto en VS Code
3. Click derecho en `index.html`
4. Selecciona "Open with Live Server"
5. ¡Listo! Se abre automáticamente

**Ventaja:** Auto-refresh cuando editas archivos

---

## ✅ Verificaciones Importantes

Una vez que el servidor esté corriendo:

### 1. Verificar que la página carga

- ✅ Deberías ver el encabezado "🤖 MoodBot"
- ✅ Mensaje de bienvenida del bot
- ✅ Textarea para escribir
- ✅ Botón de enviar (deshabilitado inicialmente)

### 2. Verificar estado de la API

Mira la parte inferior de la página:

- **🟢 API conectada** = ¡Perfecto! Todo funciona
- **🔴 API no disponible** = Espera 30-60 segundos (cold start de Render)

### 3. Probar el chat

Escribe alguno de estos mensajes de prueba:

**Test 1: Neutral**
```
Hoy fue un día normal en el trabajo. Terminé mis tareas y ahora voy a descansar.
```

**Test 2: Ansiedad**
```
Estoy muy nervioso por los exámenes finales. No puedo dejar de pensar en ello y me cuesta dormir.
```

**Test 3: Depresión**
```
Me siento muy triste y sin energía. No tengo ganas de hacer nada y todo me parece sin sentido.
```

### 4. Verificar la respuesta

Después de enviar, deberías ver:

- ✅ Tu mensaje aparece en el chat (azul, a la derecha)
- ✅ Indicador de "escribiendo" (3 puntos)
- ✅ Respuesta del bot aparece (blanco, a la izquierda)
- ✅ Card de resultado con:
  - Emoji correspondiente (🟢/🟡/🔴)
  - Clasificación (Neutral/Ansiedad/Depresión)
  - Badge de confianza (%)
  - Mensaje empático
  - Análisis detallado (desplegable)

---

## 🔍 Checklist de Testing

Marca lo que funciona:

### Visual
- [ ] El diseño se ve bien
- [ ] Los colores son correctos
- [ ] Las animaciones son suaves
- [ ] El chat es scrolleable
- [ ] Responsive en móvil (prueba redimensionando la ventana)

### Funcionalidad
- [ ] El textarea se expande al escribir
- [ ] El contador de caracteres funciona (0/1000)
- [ ] El botón se habilita cuando hay texto
- [ ] Enter envía el mensaje
- [ ] Shift+Enter hace nueva línea
- [ ] La API responde correctamente
- [ ] Los resultados se muestran bien
- [ ] Las barras de probabilidad funcionan

### API
- [ ] Health check funciona (🟢 en la parte inferior)
- [ ] Las predicciones son rápidas (<3 segundos)
- [ ] Los mensajes de error se muestran bien

---

## 🐛 Problemas Comunes y Soluciones

### Problema 1: "API no disponible" (🔴)

**Causa:** La API en Render está dormida (free tier)

**Solución:**
1. Espera 30-60 segundos
2. Verifica manualmente: https://moodbot-api.onrender.com/health
3. Si después de 2 minutos sigue en rojo, revisa los logs de Render

---

### Problema 2: Los estilos no se cargan

**Síntomas:** Página sin colores, texto plano

**Solución:**
1. Verifica que `styles.css` está en la misma carpeta
2. Abre la consola del navegador (F12)
3. Busca errores 404
4. Recarga con Ctrl+Shift+R (hard refresh)

---

### Problema 3: JavaScript no funciona

**Síntomas:** El botón no hace nada, no hay respuestas

**Solución:**
1. Abre la consola del navegador (F12)
2. Ve a la pestaña "Console"
3. Busca errores en rojo
4. Verifica que `script.js` está en la misma carpeta
5. Verifica que la ruta en index.html es correcta:
   ```html
   <script src="script.js"></script>
   ```

---

### Problema 4: CORS Error

**Síntomas:** Error en consola que menciona "CORS"

**Solución:**
- Usa el `server.py` que incluye headers CORS
- O usa la extensión "Allow CORS" en tu navegador (solo para testing)

---

### Problema 5: El servidor no inicia

**Error:** `python: command not found`

**Solución:**
```bash
# En Windows, prueba:
py server.py

# O con Python 3 específicamente:
python3 server.py
```

**Error:** `Address already in use`

**Solución:**
```bash
# Cambia el puerto en server.py de 8000 a 8001
# O cierra el proceso que está usando el puerto 8000
```

---

## 🎨 Testing de Responsive

### Desktop (1920x1080)
1. Ventana completa
2. Verifica que todo se ve espacioso
3. Márgenes correctos

### Tablet (768px)
1. Redimensiona la ventana del navegador
2. O abre DevTools (F12) → Toggle device toolbar
3. Selecciona "iPad"
4. Verifica que se adapta bien

### Mobile (375px)
1. En DevTools selecciona "iPhone SE"
2. Verifica:
   - Chat ocupa toda la pantalla
   - Mensajes no se cortan
   - Botones son clickeables
   - Keyboard no tapa el input

---

## 📸 Screenshots de Prueba

Captura pantallas de:
1. Vista inicial con mensaje de bienvenida
2. Ejemplo de conversación
3. Resultado Neutral (🟢)
4. Resultado Ansiedad (🟡)
5. Resultado Depresión (🔴)
6. Vista mobile

Estas te servirán para documentación y portfolio.

---

## ✏️ Testing de Ajustes

Antes de deployar, prueba estos ajustes:

### Cambiar colores
En `styles.css` líneas 2-7, cambia:
```css
--primary-color: #6366f1;      /* Prueba: #3b82f6 */
--neutral-color: #10b981;      /* Prueba: #22c55e */
```
Recarga (F5) y ve los cambios.

### Cambiar mensajes
En `script.js` línea ~215, modifica los mensajes empáticos:
```javascript
'Neutral': [
    "¡Tu mensaje suena muy bien!",  // Personaliza
    "Detecté estabilidad emocional."
],
```
Recarga y prueba.

### Ajustar velocidad de animaciones
En `styles.css` busca `transition:` y cambia los tiempos:
```css
transition: transform 0.2s;  /* Cambia a 0.5s para más lento */
```

---

## 📋 Checklist Final Antes de Deploy

- [ ] Probaste en Chrome/Edge
- [ ] Probaste en Firefox (opcional)
- [ ] Probaste en Safari (si tienes Mac)
- [ ] Probaste en mobile (DevTools)
- [ ] La API responde correctamente
- [ ] No hay errores en consola
- [ ] Los colores te gustan
- [ ] Los mensajes son apropiados
- [ ] Las animaciones son suaves
- [ ] Tomaste screenshots
- [ ] Todo funciona como esperabas

---

## ✅ Si Todo Funciona...

¡Estás listo para el deploy! 🚀

Avísame cuando hayas probado todo y te ayudo con el deployment en Vercel.

---

## 📞 Durante el Testing

Anota cualquier cosa que quieras cambiar:

**Ajustes visuales:**
- [ ] Colores
- [ ] Tamaños de fuente
- [ ] Espaciados
- [ ] Animaciones

**Ajustes funcionales:**
- [ ] Mensajes del bot
- [ ] Textos de la interfaz
- [ ] Comportamiento del chat
- [ ] Validaciones

**Bugs encontrados:**
- [ ] (Anota aquí)

---

<div align="center">

**🧪 ¡Buena suerte con el testing!**

Cuando termines, avísame qué ajustes quieres hacer.

</div>
