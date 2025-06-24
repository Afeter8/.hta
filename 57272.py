import os
import time
import json
import hashlib
import requests
import subprocess
from web3 import Web3

# Configuración
NODOS = [
    "http://nodo1.startigo.net:8545",
    "http://nodo2.startigo.net:8545"
]
INFURA_URL = os.getenv("INFURA_URL", "https://mainnet.infura.io/v3/TU_TOKEN")
CONTRATO_DIR = Web3.to_checksum_address("0xTU_CONTRATO")
ABI = [...]  # ABI del contrato ProteccionFGME
ARCHIVOS_SYNC = ["inmutable.py", "proteccion.py", "config.json"]

# Conexión Web3
w3 = Web3(Web3.HTTPProvider(INFURA_URL))
contract = w3.eth.contract(address=CONTRATO_DIR, abi=ABI)

# Funciones clave

def obtener_hash(path):
    with open(path, "rb") as f:
        return Web3.to_hex(Web3.keccak(text=hashlib.sha512(f.read()).hexdigest()))

def validar_hash(path):
    h = obtener_hash(path)
    try:
        return contract.functions.verificarHash(h).call()
    except:
        return False

def actualizar_archivo(archivo):
    url = f"https://raw.githubusercontent.com/FGME/repos/main/{archivo}"
    contenido = requests.get(url).content
    with open(archivo, "wb") as f:
        f.write(contenido)
    print(f"[🔄] {archivo} actualizado desde GitHub.")

def sincronizar_nodo(nodo):
    for archivo in ARCHIVOS_SYNC:
        if not validar_hash(archivo):
            print(f"[!] {archivo} inválido. Actualizando en nodo {nodo}")
            actualizar_archivo(archivo)
        else:
            print(f"[✔] {archivo} verificado en nodo {nodo}")
    # Reiniciar servicio si es necesario
    subprocess.call(["systemctl", "restart", "fgme-nodo.service"])
    print(f"[🚀] Nodo {nodo} reiniciado correctamente.")

# Bucle eterno

if __name__ == "__main__":
    while True:
        for nodo in NODOS:
            print(f"\n=== Verificando nodo {nodo} ===")
            sincronizar_nodo(nodo)
        print("\n🛡️ Todos los nodos sincronizados. Próxima ronda en 10 min.")
        time.sleep(600)
