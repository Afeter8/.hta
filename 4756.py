import hashlib, json, time

def hash_data(file_path):
    with open(file_path, 'r') as f:
        contenido = f.read()
    return hashlib.sha256(contenido.encode()).hexdigest()

def verificar_documento(nombre, esperado):
    hash_actual = hash_data(nombre)
    if hash_actual != esperado:
        raise Exception(f"⚠️ Documento {nombre} alterado o clonado.")
    print(f"✅ {nombre} verificado correctamente.")

def bucle_verificacion():
    while True:
        verificar_documento("ine_digital_encriptada.json", "2f1c9b1e...abc")
        verificar_documento("curp_digital_firmado.json", "feab123...xyz")
        time.sleep(30)

if __name__ == "__main__":
    print("🔐 Protección de INE y CURP activa para FGME")
    bucle_verificacion()
