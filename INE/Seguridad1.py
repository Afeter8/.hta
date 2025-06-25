import json, time
import hashlib

def hash_archivo(path):
    with open(path) as f:
        return hashlib.sha256(f.read().encode()).hexdigest()

def activar_defensa(pais_file):
    with open(pais_file) as f:
        data = json.load(f)
    if data["nivel_alerta"] != "verde":
        print(f"🛡️ Activando defensa en {data['pais']}: {data['protocolos_autorizados']}")
    else:
        print(f"✅ Estado seguro en {data['pais']}")

def bucle_defensa():
    paises = ["mexico_defensa.json", "iran_defensa.json", "usa_defensa.json"]
    while True:
        for p in paises:
            activar_defensa(f"paises_defensa/{p}")
        time.sleep(10)

if __name__ == "__main__":
    print("🚨 StarTigo ShieldNet IA activada")
    bucle_defensa()
