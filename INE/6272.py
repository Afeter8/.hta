import time, json, hashlib

def hash_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def verificar_integridad():
    esperado = "abc123...firmado"
    actual = hash_file("identidad_firmada.json")
    if actual != esperado:
        activar_rescate("ALERTA: Identidad modificada o alterada")
    else:
        print("🛡️ Integridad validada para Fernando")

def bucle_defensa():
    while True:
        verificar_integridad()
        time.sleep(10)

bucle_defensa()
