# 🤖 MoodBot Frontend

Frontend web para MoodBot - Clasificador de Estados Emocionales con Machine Learning

## 📋 Descripción

Interfaz de usuario tipo chatbot que permite a los usuarios analizar sus estados emocionales en tiempo real. El frontend se conecta a la API de MoodBot desplegada en Render para realizar las predicciones.

## ✨ Características

- 💬 Interfaz de chat intuitiva y moderna
- 🎨 Diseño responsive (móvil y desktop)
- 🎯 Análisis emocional en tiempo real
- 📊 Visualización de probabilidades con barras de progreso
- ⚡ Indicador de estado de la API
- 🔔 Notificaciones de error elegantes
- ♿ Accesible y fácil de usar
- 🎭 Animaciones suaves y profesionales

## 🛠️ Tecnologías

- **HTML5**: Estructura semántica
- **CSS3**: Diseño moderno con gradientes y animaciones
- **Vanilla JavaScript**: Lógica sin dependencias
- **Fetch API**: Comunicación con el backend
- **Vercel**: Hosting y deployment

## 📁 Estructura del Proyecto

```
moodbot-frontend/
├── index.html          # Página principal
├── styles.css          # Estilos y diseño
├── script.js           # Lógica y API calls
├── vercel.json         # Configuración de Vercel
├── .gitignore          # Archivos ignorados
└── README.md           # Esta documentación
```

## 🚀 Deployment en Vercel

### Opción 1: Vercel CLI (Rápido)

```bash
# 1. Instalar Vercel CLI
npm install -g vercel

# 2. Login en Vercel
vercel login

# 3. Deploy
vercel --prod
```

### Opción 2: GitHub Integration (Recomendado)

1. **Crear repositorio en GitHub**

```bash
# Inicializar Git
git init

# Añadir archivos
git add .
git commit -m "Initial commit: MoodBot Frontend"

# Subir a GitHub
gh repo create moodbot-frontend --public --source=. --remote=origin --push
```

2. **Conectar con Vercel**

- Ve a [vercel.com](https://vercel.com)
- Click en "Add New Project"
- Importa tu repositorio `moodbot-frontend`
- Vercel detectará automáticamente la configuración
- Click en "Deploy"

3. **Configurar el proyecto**

Vercel usará automáticamente la configuración en `vercel.json`. No necesitas configuración adicional.

## 🔧 Configuración

### URL de la API

Por defecto, el frontend apunta a:
```javascript
const API_URL = 'https://moodbot-api.onrender.com';
```

Si necesitas cambiar la URL de la API, edita `script.js`:

```javascript
// En script.js, línea 2
const API_URL = 'https://tu-nueva-api-url.com';
```

### Variables de Entorno (Opcional)

Si prefieres usar variables de entorno:

1. Crea un archivo `.env` (no commitear):
```bash
API_URL=https://moodbot-api.onrender.com
```

2. En Vercel Dashboard → Settings → Environment Variables:
```
NEXT_PUBLIC_API_URL = https://moodbot-api.onrender.com
```

3. Modifica `script.js`:
```javascript
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'https://moodbot-api.onrender.com';
```

## 🧪 Testing Local

### Servidor Local Simple

**Opción 1: Python**
```bash
# Python 3
python -m http.server 8000

# Abrir: http://localhost:8000
```

**Opción 2: Node.js**
```bash
# Instalar http-server
npm install -g http-server

# Ejecutar
http-server -p 8000

# Abrir: http://localhost:8000
```

**Opción 3: Live Server (VS Code)**
- Instalar extensión "Live Server"
- Click derecho en `index.html` → "Open with Live Server"

## 📊 Funcionalidades Implementadas

### 1. Health Check Automático
- Verifica la conexión con la API al cargar
- Muestra estado visual (🟢 conectado, 🔴 desconectado)
- Reintenta automáticamente en caso de fallo

### 2. Chat Interface
- Textarea auto-expandible
- Contador de caracteres (límite 1000)
- Enter para enviar (Shift+Enter para nueva línea)
- Indicador de "escribiendo" mientras procesa

### 3. Visualización de Resultados
- Cards codificados por color según emoción
  - 🟢 Verde: Neutral
  - 🟡 Amarillo: Ansiedad
  - 🔴 Rojo: Depresión
- Badge de confianza
- Mensaje empático personalizado
- Análisis detallado con barras de probabilidad

### 4. Manejo de Errores
- Notificaciones elegantes para errores
- Mensajes de error descriptivos
- Timeout handling
- Reintentos automáticos

## 🎨 Personalización

### Cambiar Colores

Edita las variables CSS en `styles.css`:

```css
:root {
    --primary-color: #6366f1;      /* Color principal */
    --secondary-color: #8b5cf6;    /* Color secundario */
    --neutral-color: #10b981;      /* Verde (Neutral) */
    --anxiety-color: #f59e0b;      /* Amarillo (Ansiedad) */
    --depression-color: #ef4444;   /* Rojo (Depresión) */
}
```

### Cambiar Fuente

```css
:root {
    --font-family: 'Tu Fuente', sans-serif;
}
```

### Modificar Mensajes

Edita los mensajes en `script.js`:

```javascript
// Línea ~200
const emoji = {
    'Neutral': '🟢',
    'Anxiety': '🟡',
    'Depression': '🔴'
}[prediction];
```

## 📱 Responsive Design

El frontend está optimizado para:

- **Desktop**: 1920x1080 y superiores
- **Tablet**: 768px - 1024px
- **Mobile**: 320px - 767px

Breakpoints principales:
```css
@media (max-width: 768px) { /* Tablet y móvil */ }
@media (max-width: 480px) { /* Solo móvil */ }
```

## ⚡ Optimización

### Performance
- Sin dependencias externas (Vanilla JS)
- CSS optimizado con variables
- Lazy loading de imágenes (si se añaden)
- Código minificado en producción (Vercel lo hace automáticamente)

### SEO
- Meta tags apropiados
- Semantic HTML
- Accesibilidad (ARIA labels donde sea necesario)

## 🔒 Seguridad

Medidas implementadas:
- Escape de HTML para prevenir XSS
- Headers de seguridad en `vercel.json`
- Validación de input (longitud máxima)
- HTTPS por defecto en Vercel

## 🐛 Troubleshooting

### La API no responde

**Síntoma**: Indicador rojo, mensajes de error

**Soluciones**:
1. Verificar que la API esté en línea: https://moodbot-api.onrender.com/health
2. Esperar 30-60 segundos (cold start de Render free tier)
3. Revisar consola del navegador (F12) para errores
4. Verificar CORS si la URL cambió

### El chat no envía mensajes

**Soluciones**:
1. Verificar que el textarea tenga texto
2. Abrir consola (F12) y buscar errores de JavaScript
3. Verificar conexión a internet
4. Limpiar caché del navegador

### Estilos no se cargan

**Soluciones**:
1. Hard refresh: Ctrl+Shift+R (Windows) o Cmd+Shift+R (Mac)
2. Verificar que `styles.css` esté en el mismo directorio
3. Revisar la consola para errores 404

## 📈 Métricas y Analytics (Opcional)

Para añadir Google Analytics:

```html
<!-- En <head> de index.html -->
<script async src="https://www.googletagmanager.com/gtag/js?id=TU-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'TU-ID');
</script>
```

## 🔮 Mejoras Futuras

- [ ] Historial de conversaciones (localStorage)
- [ ] Exportar conversación como PDF
- [ ] Modo oscuro
- [ ] Selector de idioma
- [ ] Gráficos de tendencia emocional
- [ ] Integración con autenticación
- [ ] PWA (Progressive Web App)
- [ ] Share API para compartir resultados

## 🤝 Contribuciones

Si quieres contribuir:

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

## 👤 Autor

**Angie Díaz**
- GitHub: [@AngieDiaz25](https://github.com/AngieDiaz25)
- Email: [tu-email@ejemplo.com]

## 🙏 Agradecimientos

- Backend API desarrollado con Flask + scikit-learn
- Iconos y emojis nativos del sistema
- Fuente: Inter (Google Fonts)
- Hosting: Vercel

---

## 📞 Soporte

¿Problemas o preguntas?

1. Revisa esta documentación
2. Consulta la [documentación de la API](../API_GUIDE.md)
3. Abre un issue en GitHub
4. Contacta al desarrollador

---

<div align="center">

**MoodBot Frontend v1.0.0**

Hecho con ❤️ por Angie Díaz

[Demo](https://moodbot-frontend.vercel.app) • [API](https://moodbot-api.onrender.com) • [GitHub](https://github.com/AngieDiaz25)

</div>
