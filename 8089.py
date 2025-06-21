import hashlib
import os
import time
import subprocess
import logging

# Configuración de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Archivo de configuración inmutable
CONFIG_JSON = "reparacion_inmutable.json"

# Función para obtener hash SHA-256 de un archivo
def get_file_hash(path):
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

# Función para ejecutar comandos según sistema
def reparar_sistema(nombre, accion):
    logging.info(f"🔧 Reparando: {nombre}")
    try:
        subprocess.run(accion, shell=True, check=True)
        logging.info(f"✅ {nombre} reparado correctamente")
    except subprocess.CalledProcessError as e:
        logging.error(f"❌ Error al reparar {nombre}: {e}")

# Diccionario de acciones (puede ser externo con JSON)
REPARACIONES = {
    "Windows": "sfc /scannow",
    "Linux": "apt-get --fix-broken install -y",
    "Red IP": "ipconfig /renew" if os.name == "nt" else "dhclient",
    "HTML": "python3 html_linter.py",
    "UEFI": "fwupdmgr get-updates",
    "BIOS": "fwupdmgr update",
}

# Hash de verificación (simulado)
EXPECTED_HASH = "edb0f1822c1f4dba9d4a3f19b6de9b59f3b3a4c74857cc304ef20e289dc9e7a7"

def verificacion_inmutable():
    logging.info("🛡️ Verificando integridad del script...")
    current_hash = get_file_hash(__file__)
    if current_hash != EXPECTED_HASH:
        logging.critical("⚠️ ALERTA: Código alterado. Abortando operación.")
        exit(1)
    logging.info("🔒 Código verificado como inmutable")

# Bucle infinito (puede ajustarse a cron o trigger IA)
def bucle_reparacion():
    while True:
        verificacion_inmutable()
        for sistema, comando in REPARACIONES.items():
            reparar_sistema(sistema, comando)
        logging.info("♻️ Esperando para siguiente ciclo...")
        time.sleep(1800)  # 30 minutos entre ciclos (ajustable)

if __name__ == "__main__":
    logging.info("🔁 Sistema de reparación inmutable iniciado")
    bucle_reparacion()
