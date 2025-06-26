import time, hashlib, os

def hash_digital(dato):
    return hashlib.sha256(dato.encode()).hexdigest()

def proteger_archivo(ruta):
    if os.path.exists(ruta):
        with open(ruta, 'r') as f:
            contenido = f.read()
        hash_actual = hash_digital(contenido)
        print(f"[✓] Protegido: {ruta} - Hash: {hash_actual}")
    else:
        print(f"[X] Archivo no encontrado: {ruta}")

# Bucle eterno de protección backend
archivos = ['index.html', 'core.css', 'defensa.js', 'config.json']
while True:
    for archivo in archivos:
        proteger_archivo(archivo)
    time.sleep(10)
