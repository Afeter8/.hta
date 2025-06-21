import hashlib
import os
import time
import threading
import logging

# Activar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Configuración principal
CONFIG = {
    "autor": "Fernando Guadalupe Mendez Espinoza",
    "rotacion_intervalo": 60,  # segundos
    "archivos_a_proteger": ["inmutable.json", "main.html", "core.js"],
    "modo_autonomo": True,
    "proteccion_hash": True,
    "algoritmo_hash": "sha256",
    "bucles_eternos": True
}

# Hash original de referencia para verificación de integridad
hashes_referencia = {}

def calcular_hash(path, algoritmo="sha256"):
    if not os.path.exists(path):
        return None
    h = hashlib.new(algoritmo)
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def verificar_integridad():
    for archivo in CONFIG["archivos_a_proteger"]:
        hash_actual = calcular_hash(archivo)
        hash_esperado = hashes_referencia.get(archivo)
        if hash_actual != hash_esperado:
            logging.warning(f"⚠️ Alteración detectada en {archivo}. Restaurando...")
            restaurar_archivo(archivo)
        else:
            logging.info(f"✅ {archivo} verificado correctamente.")

def guardar_hashes_iniciales():
    for archivo in CONFIG["archivos_a_proteger"]:
        hashes_referencia[archivo] = calcular_hash(archivo)

def restaurar_archivo(nombre_archivo):
    # Simulación de restauración (usar backup o IPFS real en producción)
    with open(nombre_archivo, "w") as f:
        f.write("// Código restaurado automáticamente por IA inmutable\n")

def rotar_codigo():
    while CONFIG["bucles_eternos"]:
        verificar_integridad()
        logging.info("🌀 Rotación de seguridad ejecutada.")
        time.sleep(CONFIG["rotacion_intervalo"])

def iniciar_defensa():
    guardar_hashes_iniciales()
    if CONFIG["modo_autonomo"]:
        logging.info("🔐 Sistema de protección inmutable activado.")
        threading.Thread(target=rotar_codigo, daemon=True).start()

if __name__ == "__main__":
    iniciar_defensa()
    while True:
        time.sleep(1)  # Mantiene el sistema vivo
