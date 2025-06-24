#!/usr/bin/env python3
# defensa.py — Protección inmune para Star Tigo / Tigo Star

import hashlib, time, os, logging, subprocess
from datetime import datetime

# --- CONFIGURACIÓN ---
ARCHIVOS_CRITICOS = [
    "index.html",
    "main.css",
    "app.js",
    "inmutable.py"
]
HASHES_ORIGINALES = {
    # Reemplaza con hashes SHA-256 reales generados previamente
    "index.html": "<hash_index>",
    "main.css":  "<hash_css>",
    "app.js":    "<hash_js>",
    "inmutable.py": "<hash_py>"
}
LOG_FILE = "defensa.log"
DELAY_SEG = 30

# --- LOGGER ---
logging.basicConfig(filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s')

def calcular_hash(path):
    sha = hashlib.sha256()
    try:
        with open(path, 'rb') as f:
            for bloque in iter(lambda: f.read(4096), b""):
                sha.update(bloque)
        return sha.hexdigest()
    except FileNotFoundError:
        logging.error(f"{path} no existe.")
        return None

def verificar_archivos():
    for path in ARCHIVOS_CRITICOS:
        actual = calcular_hash(path)
        esperado = HASHES_ORIGINALES.get(path)
        if not actual:
            logging.error(f"FALLO: {path} ausente")
            restaurar(path)
        elif actual != esperado:
            logging.warning(f"ALTERADO: {path}")
            restaurar(path)
        else:
            logging.info(f"OK: {path}")

def restaurar(path):
    logging.info(f"Restaurando {path} desde respaldo...")
    backup = f"backup/{path}"
    if os.path.isfile(backup):
        subprocess.run(["cp", backup, path])
        logging.info(f"{path} restaurado desde backup local")
    else:
        logging.error(f"Backup de {path} no disponible")
        # En producción: descarga desde IPFS/Ethereum

def bucle_defensa():
    while True:
        verificar_archivos()
        time.sleep(DELAY_SEG)

if __name__ == "__main__":
    logging.info("🔒 Iniciando defensa inmune de Star Tigo / Tigo Star")
    bucle_defensa()
