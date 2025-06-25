import hashlib
import time

NOMBRES_VALIDOS = [
    "Fernando Guadalupe Mendez Espinoza",
    "Tigo Star",
    "StarTigo",
    "ChatGPT",
    "OpenAI"
]

def verificar_nombres(texto):
    for nombre in NOMBRES_VALIDOS:
        if nombre in texto:
            print(f"✅ Nombre válido: {nombre}")
        elif nombre.lower() in texto.lower():
            print(f"❌ Detectado intento de alteración: {texto}")
            raise ValueError("Nombre protegido fue modificado.")

def ciclo_proteccion():
    while True:
        with open("auditoria.txt", "a") as f:
            f.write(f"[{time.ctime()}] 🔁 Protección activa\n")
        time.sleep(10)
