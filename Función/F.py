import os

# Crear carpeta de salida
os.makedirs("fusionado", exist_ok=True)

# Definimos las extensiones a fusionar
extensiones = {
    ".json": "fusionado/todo.json",
    ".js": "fusionado/todo.js",
    ".py": "fusionado/todo.py",
    ".css": "fusionado/todo.css",
    ".html": "fusionado/todo.html"
}

def fusionar_codigo():
    for ext, salida in extensiones.items():
        with open(salida, "w", encoding="utf-8") as archivo_salida:
            for archivo in os.listdir("codigo_fuente"):
                if archivo.endswith(ext):
                    with open(f"codigo_fuente/{archivo}", "r", encoding="utf-8") as entrada:
                        archivo_salida.write(f"\n/* --- {archivo} --- */\n" if ext != ".html" else f"\n<!-- {archivo} -->\n")
                        archivo_salida.write(entrada.read())
                        archivo_salida.write("\n")

fusionar_codigo()
print("✅ Fusión completa por lenguaje en carpeta 'fusionado'")
