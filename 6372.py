#!/usr/bin/env python3
# defensa.py — Protección inmutable para Star Tigo y Tigo Star

import os
import hashlib
import time
import shutil
import logging

# === CONFIGURACIÓN ===
ARCHIVOS_PROTEGIDOS = [
    "index.html",
    "inmutable.css",
    "inmutable.js",
    "inmutable.json",
    "defensa.py"
]

# Hashes SHA256 válidos de cada archivo (obtenidos tras validación y respaldo)
HASHES_VALIDOS = {
    "index.html": "REEMPLAZAR_HASH1",
    "inmutable.css": "REEMPLAZAR_HASH2",
    "inmutable.js": "REEMPLAZAR_HASH3",
    "inmutable.json": "REEMPLAZAR_HASH4",
    "defensa.py": "REEMPLAZAR_HASH5"
}

RESPALDO_DIR = "./respaldo"
INTERVALO_SEGUNDOS = 15  # Tiempo entre verificaciones

# === LOG ===
logging.basicConfig(filename="defensa.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# === FUNCIONES ===
def calcular_hash(path):
    """Calcula SHA256 de un archivo"""
    sha = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                sha.update(bloque)
        return sha.hexdigest()
    except FileNotFoundError:
        return None

def restaurar_archivo(nombre):
    """Restaura archivo desde respaldo"""
    origen = os.path.join(RESPALDO_DIR, nombre)
    destino = nombre
    if os.path.exists(origen):
        shutil.copy2(origen, destino)
        logging.warning(f"{nombre} fue restaurado desde respaldo")
    else:
        logging.error(f"Respaldo de {nombre} no encontrado")

def verificar_integridad():
    """Verifica integridad de todos los archivos"""
    for archivo in ARCHIVOS_PROTEGIDOS:
        hash_actual = calcular_hash(archivo)
        hash_valido = HASHES_VALIDOS.get(archivo)
        if not hash_actual:
            logging.error(f"{archivo} está ausente. Restaurando...")
            restaurar_archivo(archivo)
        elif hash_actual != hash_valido:
            logging.warning(f"{archivo} fue modificado. Restaurando...")
            restaurar_archivo(archivo)
        else:
            logging.info(f"{archivo} verificado correctamente")

def bucle_eterno():
    """Bucle infinito de protección"""
    logging.info("🛡️ Defensa inmutable iniciada...")
    while True:
        verificar_integridad()
        time.sleep(INTERVALO_SEGUNDOS)

# === EJECUCIÓN ===
if __name__ == "__main__":
    bucle_eterno()
