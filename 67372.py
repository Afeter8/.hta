import os import time import hashlib import subprocess import random from web3 import Web3

Conexión Ethereum (puede ser Geth local o Infura)

web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/TU_TOKEN_INFURA")) contract_address = Web3.to_checksum_address("0xTU_CONTRATO") contract_abi = [ { "inputs": [{"internalType": "bytes32", "name": "_hash", "type": "bytes32"}], "name": "verificarHash", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function" } ] contract = web3.eth.contract(address=contract_address, abi=contract_abi)

Codificación rotativa en bucles (emojis, letras, números, binario)

def codificacion_rotativa(texto): emojis = ["🔒", "🧠", "📡", "🛰️", "🧬", "⚙️"] resultado = ''.join(random.choice([c.upper(), c.lower(), str(ord(c)%10), random.choice(emojis)]) for c in texto if c.isalnum()) return resultado

Escaneo de red LAN

def escaneo_red(): print("\n[DEFENSA] Escaneo de red LAN...") resultado = subprocess.getoutput("arp -a") print(resultado)

Escaneo de redes WiFi (RF)

def escaneo_rf(): print("\n[DEFENSA RF] Escaneo de redes WiFi...") try: redes = subprocess.check_output(["nmcli", "device", "wifi", "list"]).decode() print(redes) except: print("nmcli no disponible. Saltando RF scan...")

Verificación hash blockchain

def verificar_codigo(path): with open(path, 'rb') as f: contenido = f.read() hash_code = Web3.to_hex(Web3.keccak(text=hashlib.sha512(contenido).hexdigest())) valido = contract.functions.verificarHash(hash_code).call() codificado = codificacion_rotativa(path) print(f"\n[VERIFICACIÓN] {codificado}: {'✔️ válido' if valido else '❌ alterado'}")

Lista de archivos críticos para proteger

archivos = ["inmutable.py", "inmutable.html", "inmutable.css", "inmutable.js", "inmutable.json"]

Bucle eterno de defensa

if name == "main": while True: print("\n🔁 Iniciando ronda de protección total FGME...") escaneo_red() escaneo_rf() for archivo in archivos: if os.path.exists(archivo): verificar_codigo(archivo) print("🛡️ Defensa completada. Esperando próxima ronda...") time.sleep(180)  # Cada 3 minutos

