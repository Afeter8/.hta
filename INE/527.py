import hashlib, time, json

def hash_json(path):
    with open(path) as f:
        return hashlib.sha256(f.read().encode()).hexdigest()

def verificar():
    esperado = "3abf9d7e..."  # hash inmutable firmado
    actual = hash_json("wallet_protegida.json")
    if actual != esperado:
        raise Exception("⚠️ Alteración o intento de acceso no autorizado")
    print("✅ Sistema CESAR validado")

while True:
    verificar()
    time.sleep(10)
