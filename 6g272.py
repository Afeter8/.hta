import hashlib
import time
import os
import json

# Identidad autorizada
USUARIO_AUTORIZADO = "Fernando Guadalupe Mendez Espinoza"
FIRMA_DIGITAL = "d9c54b8e0e3f24bd27bcf9b812..."  # Simulada para verificación
ARCHIVO_VERIFICADO = "configuracion_inmutable.json"

# Función de hash para verificar integridad
def calcular_hash_archivo(nombre_archivo):
    sha256_hash = hashlib.sha256()
    with open(nombre_archivo, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Cargar configuración JSON
def cargar_configuracion():
    try:
        with open(ARCHIVO_VERIFICADO, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("[ERROR] No se pudo cargar la configuración:", e)
        return None

# Sistema de defensa automatizado
def iniciar_defensa():
    print("[🔒] Iniciando defensa inmutable...")
    configuracion = cargar_configuracion()

    if not configuracion:
        print("[❌] Configuración inválida. Sistema detenido.")
        return

    if configuracion["usuario_autorizado"] != USUARIO_AUTORIZADO:
        print("[🚨] Usuario no autorizado. Bloqueo activado.")
        return

    hash_actual = calcular_hash_archivo(ARCHIVO_VERIFICADO)
    if hash_actual != FIRMA_DIGITAL:
        print("[🛑] Manipulación detectada. Apagando sistema.")
        return

    if configuracion["modulo_defensa"]["activado"]:
        while True:
            print("[✅] Sistema en ejecución segura. Monitoreando...")
            time.sleep(5)
            # Aquí se podrían agregar sensores, conexión IA o lectura desde IPFS

# Punto de entrada
if __name__ == "__main__":
    try:
        iniciar_defensa()
    except KeyboardInterrupt:
        print("\n[⚠️] Intervención manual detectada. Sistema bloqueado.")
