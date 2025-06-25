import json, os, time
from datetime import datetime

def verificar_derechos(pais):
    path = f"paises/{pais.lower()}.json"
    if not os.path.exists(path):
        return False
    with open(path) as f:
        data = json.load(f)
    if not data.get("conexion_autorizada", False):
        print(f"⚠️ Acceso restringido por IA para {pais}")
        return False
    print(f"🛡️ {pais} aprobado: {data['derechos_civiles']}")
    return True

def bucle_ia_global():
    paises = ["mexico", "alemania", "iran", "japon"]
    while True:
        for pais in paises:
            verificar_derechos(pais)
        time.sleep(15)

if __name__ == "__main__":
    print("🌐 IA Guardian Global ejecutando...")
    bucle_ia_global()
