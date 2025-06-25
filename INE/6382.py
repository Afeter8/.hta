from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("clave.key", "wb") as f:
    f.write(key)

def cifrar(path):
    fernet = Fernet(key)
    with open(path, "rb") as file:
        original = file.read()
    cifrado = fernet.encrypt(original)
    with open(path, "wb") as file:
        file.write(cifrado)

cifrar("identidad_firmada.json")
