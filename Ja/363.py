import requests
import hashlib
import os
import json

def obtener_version_actual():
    return "14.0.0-StarTigo"

def verificar_hash(firmware_path, hash_esperado):
    with open(firmware_path, "rb") as f:
        contenido = f.read()
        return hashlib.sha256(contenido).hexdigest() == hash_esperado

def descargar_firmware(info_url):
    response = requests.get(info_url)
    metadata = response.json()

    firmware_url = metadata["firmware_url"]
    hash_esperado = metadata["sha256"]

    firmware = requests.get(firmware_url)
    with open("firmware.zip", "wb") as f:
        f.write(firmware.content)

    if verificar_hash("firmware.zip", hash_esperado):
        print("✅ Firmware verificado, listo para instalar.")
        os.system("bash ota_installer.sh")
    else:
        print("⚠️ El firmware fue alterado. Abortando actualización.")

# Ejecutar verificación
descargar_firmware("https://startigo.io/update/firmware_update.json")
