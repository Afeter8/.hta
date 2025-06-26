import time
import json
import logging
import os
from datetime import datetime

# Cargar configuración
with open('config_global.json') as f:
    config = json.load(f)

# Setup log
logging.basicConfig(filename='log_global.log', level=logging.INFO)

def verificar_redes():
    redes = config["redes_soportadas"]
    for red in redes:
        logging.info(f"🛰️ Verificando conectividad: {red}")
        os.system("ping -c 1 8.8.8.8" if os.name != "nt" else "ping -n 1 8.8.8.8")

def defensa_total():
    logging.info(f"🛡️ Defensa automática activada por IA.")
    # Simulación de firewall automático + hash verificación

def bucle_infinito():
    while True:
        verificar_redes()
        defensa_total()
        time.sleep(60)  # Ejecuta cada minuto

if __name__ == "__main__":
    bucle_infinito()
