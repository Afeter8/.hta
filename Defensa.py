# defensa.py
import hashlib, time, os

HASH_VALIDO = "a23b4f..."  # SHA256 real

def verificar_integridad(file):
    sha = hashlib.sha256()
    with open(file, "rb") as f:
        while chunk := f.read(8192):
            sha.update(chunk)
    return sha.hexdigest() == HASH_VALIDO

def defensa_total():
    archivos = ["sistema.js", "index.html", "modelo_ia.json"]
    for archivo in archivos:
        if not verificar_integridad(archivo):
            print(f"[!] Código corrupto: {archivo}")
            os.system("shutdown -h now")  # Defensa física
        else:
            print(f"[✓] {archivo} íntegro")

while True:
    defensa_total()
    time.sleep(3600)
