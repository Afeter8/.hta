# defensa.py
import hashlib
import os
import sys
import time

# Lista de archivos críticos del sistema
archivos = [
    "index.html",
    "scripts/defensa.js",
    "scripts/inmutable.js",
    "system/configuracion.json"
]

# Hashs legítimos registrados
hash_legitimos = {
    "index.html": "HASH_ORIGINAL_1",
    "scripts/defensa.js": "HASH_ORIGINAL_2",
    "scripts/inmutable.js": "HASH_ORIGINAL_3",
    "system/configuracion.json": "HASH_ORIGINAL_4"
}

def calcular_hash(path):
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def verificar_integridad():
    for archivo in archivos:
        if not os.path.exists(archivo):
            print(f"[ALERTA] Falta el archivo: {archivo}")
            return False
        hash_actual = calcular_hash(archivo)
        if hash_actual != hash_legitimos[archivo]:
            print(f"[ATAQUE DETECTADO] Modificación en {archivo}")
            return False
    return True

def defensa_total():
    while True:
        if not verificar_integridad():
            print("[⚠️ SISTEMA ALTERADO] Desactivando ejecución.")
            # Apagar el sistema, borrar claves, bloquear red, etc.
            os.system("shutdown -s -t 1")  # Windows (opcional)
            sys.exit()
        time.sleep(5)

if __name__ == "__main__":
    defensa_total()
