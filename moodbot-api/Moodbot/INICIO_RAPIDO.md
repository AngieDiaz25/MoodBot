# 🚀 Guía Rápida - MoodBot Frontend

## ✅ Archivos Incluidos

Tienes todos estos archivos listos para usar:

```
📁 moodbot-frontend/
├── 📄 index.html           # Página principal (5.8 KB)
├── 🎨 styles.css           # Estilos (13 KB)
├── ⚙️ script.js            # Lógica (12 KB)
├── 🔧 vercel.json          # Config Vercel (701 B)
├── 🚫 .gitignore           # Archivos a ignorar (329 B)
├── 📖 README_FRONTEND.md   # Documentación completa (8 KB)
└── 📋 INICIO_RAPIDO.md     # Esta guía
```

---

## 🎯 Deploy en 3 Pasos (5 minutos)

### Paso 1: Crear repositorio en GitHub

```bash
# Navega a la carpeta donde descargaste los archivos
cd moodbot-frontend

# Inicializa Git
git init

# Añade los archivos
git add .

# Primer commit
git commit -m "Initial commit: MoodBot Frontend"

# Crea el repositorio en GitHub y súbelo (con GitHub CLI)
gh auth login
gh repo create moodbot-frontend --public --source=. --remote=origin --push
```

### Paso 2: Conectar con Vercel

1. Ve a [vercel.com](https://vercel.com)
2. Click en **"Add New Project"**
3. Click en **"Import Git Repository"**
4. Selecciona tu repo `moodbot-frontend`
5. Click en **"Deploy"**

### Paso 3: ¡Listo! 🎉

Tu frontend estará en línea en ~30 segundos en una URL como:
```
https://moodbot-frontend.vercel.app
```

---

## 🧪 Probar Localmente ANTES de Deploy

Si quieres ver cómo se ve antes de deployar:

### Opción 1: Python (más fácil)
```bash
# Abre la terminal en la carpeta del proyecto
python -m http.server 8000

# Abre tu navegador en:
# http://localhost:8000
```

### Opción 2: Node.js
```bash
npx http-server -p 8000

# Abre tu navegador en:
# http://localhost:8000
```

### Opción 3: VS Code
1. Instala la extensión "Live Server"
2. Click derecho en `index.html`
3. Selecciona "Open with Live Server"

---

## 🔍 Verificar que Todo Funciona

1. **Abrir la página**: Deberías ver el chatbot MoodBot
2. **Verificar API**: En la parte inferior debería decir "🟢 API conectada"
   - Si dice "🔴 API no disponible", espera 30-60 segundos (cold start de Render)
3. **Probar el chat**: Escribe algo como "Me siento muy bien hoy"
4. **Ver resultado**: Deberías ver la predicción del estado emocional

---

## ⚙️ Configuración de la API

Por defecto, el frontend apunta a tu API en Render:
```
https://moodbot-api.onrender.com
```

Si necesitas cambiar la URL, edita `script.js` línea 2:
```javascript
const API_URL = 'https://tu-nueva-url-api.com';
```

---

## 📱 Características del Frontend

✨ **Lo que tiene tu frontend:**

- ✅ Interfaz de chat moderna y responsive
- ✅ Conexión automática a tu API de ML
- ✅ Indicador de estado de la API
- ✅ Visualización de probabilidades con barras
- ✅ Mensajes empáticos personalizados
- ✅ Diseño codificado por colores:
  - 🟢 Verde = Neutral
  - 🟡 Amarillo = Ansiedad
  - 🔴 Rojo = Depresión
- ✅ Auto-resize del textarea
- ✅ Contador de caracteres
- ✅ Animaciones suaves
- ✅ Compatible con móviles

---

## 🎨 Personalización Rápida

### Cambiar colores principales

Edita `styles.css` líneas 2-7:
```css
:root {
    --primary-color: #6366f1;      /* Azul principal */
    --secondary-color: #8b5cf6;    /* Morado secundario */
    --neutral-color: #10b981;      /* Verde (Neutral) */
    --anxiety-color: #f59e0b;      /* Amarillo (Ansiedad) */
    --depression-color: #ef4444;   /* Rojo (Depresión) */
}
```

### Cambiar título

Edita `index.html` línea 9:
```html
<title>MoodBot - Tu Título Aquí</title>
```

---

## 🐛 Solución de Problemas Comunes

### Problema 1: "API no disponible"
**Solución**: Espera 30-60 segundos. La API en Render free tier se "duerme" y tarda en despertar.

### Problema 2: Los estilos no se ven
**Solución**: 
- Asegúrate de que `styles.css` está en la misma carpeta que `index.html`
- Haz hard refresh: Ctrl+Shift+R (Windows) o Cmd+Shift+R (Mac)

### Problema 3: JavaScript no funciona
**Solución**:
- Abre la consola del navegador (F12)
- Busca errores en rojo
- Verifica que `script.js` esté en la misma carpeta

---

## 📚 Documentación Completa

Para más detalles, consulta:

- **README_FRONTEND.md**: Documentación completa del frontend
- **API_GUIDE.md**: Documentación de la API
- **DEPLOYMENT.md**: Guía detallada de deployment

---

## ✅ Checklist de Deploy

Antes de hacer deploy, verifica:

- [ ] Todos los archivos están en la misma carpeta
- [ ] La API está funcionando en Render
- [ ] Probaste localmente y funciona
- [ ] Git está inicializado
- [ ] Repositorio creado en GitHub
- [ ] Código subido a GitHub
- [ ] Vercel conectado al repositorio
- [ ] Deploy exitoso

---

## 🎉 ¡Y eso es todo!

Tu frontend debería estar funcionando perfectamente. Ahora tienes:

✅ **Backend**: API en Render  
✅ **Frontend**: Interfaz en Vercel  
✅ **Documentación**: Completa y profesional  
✅ **Proyecto**: Listo para mostrar  

---

## 📞 ¿Necesitas Ayuda?

Si algo no funciona:

1. Revisa esta guía de nuevo
2. Consulta README_FRONTEND.md
3. Verifica los logs de Vercel
4. Abre la consola del navegador (F12)

---

<div align="center">

**¡Éxito con tu proyecto MoodBot! 🤖✨**

Desarrollado con ❤️ por Angie Díaz

</div>
