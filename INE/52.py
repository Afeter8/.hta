from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open("clave_cesar.key", "wb") as f:
    f.write(key)

def cifrar_archivo(archivo):
    fernet = Fernet(key)
    with open(archivo, "rb") as file:
        original = file.read()
    encriptado = fernet.encrypt(original)
    with open(archivo, "wb") as file:
        file.write(encriptado)

cifrar_archivo("wallet_protegida.json")
