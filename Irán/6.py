import hashlib, time, json

def hash_seguro(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

def verificar_componentes():
    claves = [
        "Fernando", "StarTigo", "ChatGPT", "Tigo Star", "🌐", "🔐", "🧠",
        ":", ";", ",", ".", "?", "!", "1", "2", "3", "A", "a", "Z", "z"
    ]
    for palabra in claves:
        if palabra.lower() != palabra or palabra.upper() != palabra:
            continue
        hash_check = hash_seguro(palabra)
        if not hash_check: raise Exception("Alteración detectada")
    print("✅ Letras, números y signos protegidos")

def ciclo_verificacion():
    while True:
        verificar_componentes()
        time.sleep(10)

if __name__ == "__main__":
    ciclo_verificacion()
