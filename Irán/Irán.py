import hashlib, time, json
from datetime import datetime
from web3 import Web3  # Ethereum conexión

# Conexión a red descentralizada (Ethereum/IPFS opcional)
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/TU_API_KEY"))

def calcular_hash(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

def guardar_en_blockchain(data):
    hash_data = calcular_hash(data)
    # Enviar a blockchain/IPFS (simulado)
    print(f"🔗 Hash registrado en blockchain: {hash_data}")
    return hash_data

def bucle_guardian():
    while True:
        with open("json_config.json") as f:
            config = json.load(f)
        hash_actual = calcular_hash(config)
        if config.get("hash_sha256") != hash_actual:
            print("⚠️ Alteración detectada. Desconectando módulo.")
            break
        print("🛡️ Sistema descentralizado íntegro.")
        time.sleep(10)

if __name__ == "__main__":
    print("🚀 Guardian IA StarTigo activo")
    bucle_guardian()
