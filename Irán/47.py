# guardian_descentralizado.py

from web3 import Web3
import json, time

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/TU_API"))

def verificar_estado():
    contract = w3.eth.contract(address='0x...', abi=json.load(open('abi.json')))
    hash_en_chain = contract.functions.getEstado().call()
    with open("sistema.json") as f:
        local_hash = json.load(f).get("hash")
    return hash_en_chain == local_hash

while True:
    if verificar_estado():
        print("✅ Sistema descentralizado y válido")
    else:
        print("⚠️ Alteración detectada. Bloqueo IA.")
    time.sleep(15)
