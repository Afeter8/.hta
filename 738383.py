import os import time import hashlib import subprocess from web3 import Web3

Conexión Ethereum (puede ser Geth local o Infura)

web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/TU_TOKEN_INFURA")) contract_address = Web3.to_checksum_address("0xTU_CONTRATO") contract_abi = [ { "inputs": [{"internalType": "bytes32", "name": "_hash", "type": "bytes32"}], "name": "verificarHash", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function" } ] contract = web3.eth.contract(address=contract_address, abi=contract_abi)

Escaneo básico de red (ejemplo simple)

def escaneo_red(): print("\n[DEFENSA] Escaneo de red LAN...") resultado = subprocess.getoutput("arp -a") print(resultado)

Protección de RF: escaneo de interfaces WiFi (Linux)

def escaneo_rf(): print("\n[DEFENSA RF] Escaneo de redes WiFi...") try: redes = subprocess.check_output(["nmcli", "device", "wifi", "list"]).decode() print(redes) except: print("nmcli no disponible. Saltando RF scan...")

Verificación blockchain del código

def verificar_codigo(path): with open(path, 'rb') as f: contenido = f.read() hash_code = Web3.to_hex(Web3.keccak(text=hashlib.sha512(contenido).hexdigest())) valido = contract.functions.verificarHash(hash_code).call() print(f"\n[VERIFICACIÓN] {path}: {'✔️ válido' if valido else '❌ alterado'}")

Ciclo autónomo

if name == "main": while True: escaneo_red() escaneo_rf() verificar_codigo("inmutable.py") time.sleep(120)  # Cada 2 minutos

