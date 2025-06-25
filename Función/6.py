import hashlib

for archivo in os.listdir("fusionado"):
    with open(f"fusionado/{archivo}", "rb") as f:
        contenido = f.read()
        hash_result = hashlib.sha256(contenido).hexdigest()
        print(f"{archivo} 🧬 Hash: {hash_result}")
