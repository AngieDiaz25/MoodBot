#!/usr/bin/env python3
"""
Servidor local simple para MoodBot Frontend
Uso: python server.py
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Añadir headers CORS para desarrollo local
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    # Cambiar al directorio del script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    Handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"""
╔══════════════════════════════════════════════════════════╗
║            🤖 MoodBot Frontend - Servidor Local          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  ✅ Servidor iniciado correctamente                      ║
║                                                          ║
║  🌐 URL Local:    http://localhost:{PORT}                ║
║  🌐 URL Red:      http://127.0.0.1:{PORT}                ║
║                                                          ║
║  📝 Abre tu navegador en la URL de arriba               ║
║  🔄 Los cambios se verán al recargar la página          ║
║  ⛔ Presiona Ctrl+C para detener el servidor            ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
        """)
        
        # Intentar abrir el navegador automáticamente
        try:
            webbrowser.open(f'http://localhost:{PORT}')
            print("🚀 Abriendo navegador...")
        except:
            print("⚠️  No se pudo abrir el navegador automáticamente")
            print(f"   Abre manualmente: http://localhost:{PORT}")
        
        print("\n⏳ Servidor corriendo... (Ctrl+C para detener)\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Servidor detenido. ¡Hasta luego!")

if __name__ == "__main__":
    main()
