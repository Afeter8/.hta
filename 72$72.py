import os
import hashlib
import time
import logging
import requests

# Configuración básica
OWNER = "Fernando Guadalupe Mendez Espinoza"
ETH_NODE = "https://mainnet.infura.io/v3/CLAVE_PRIVADA"
INMUTABLE_FILES = ["index.html", "style.css", "sistema.json", "defensa.js"]
HASH_REGISTRO = {}

# Logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')

def calcular_hash(archivo):
    sha = hashlib.sha256()
    try:
        with open(archivo, "rb") as f:
            while chunk := f.read(8192):
                sha.update(chunk)
        return sha.hexdigest()
    except FileNotFoundError:
        return None

def verificar_integridad():
    logging.info("Verificando integridad de archivos inmutables...")
    for archivo in INMUTABLE_FILES:
        hash_actual = calcular_hash(archivo)
        hash_guardado = HASH_REGISTRO.get(archivo)
        if hash_guardado and hash_actual != hash_guardado:
            logging.warning(f"ALERTA: Modificación detectada en {archivo}. Intentando restaurar...")
            reparar_archivo(archivo)
        else:
            logging.info(f"{archivo} verificado correctamente.")

def registrar_hashes():
    for archivo in INMUTABLE_FILES:
        hash_valor = calcular_hash(archivo)
        if hash_valor:
            HASH_REGISTRO[archivo] = hash_valor
    logging.info("Hashes registrados para todos los archivos protegidos.")

def reparar_archivo(nombre_archivo):
    # Aquí puedes integrar una recuperación desde IPFS, backup local o código blockchain
    logging.critical(f"Archivo {nombre_archivo} ha sido modificado. Enviar alerta a Ethereum.")
    # Simulación: eliminar archivo dañado
    try:
        os.remove(nombre_archivo)
    except:
        pass
    # Simulación de restauración automática
    with open(nombre_archivo, "w") as f:
        f.write("// Archivo restaurado por IA - modo seguro")

def loop_eterno():
    logging.info(f"Inicio de defensa en bucle eterno para {OWNER}")
    registrar_hashes()
    while True:
        verificar_integridad()
        time.sleep(10)

if __name__ == "__main__":
    loop_eterno()
