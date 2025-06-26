# totalplay_defensa.py
import os
import time
import socket
import logging
import platform
import subprocess

# === Configuración de logs ===
logging.basicConfig(filename='totalplay_eventos.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# === Información del sistema ===
usuario = os.getenv('USERNAME') or os.getenv('USER')
sistema = platform.system()

def verificar_conexion():
    try:
        socket.create_connection(("8.8.8.8", 53))
        return True
    except:
        return False

def escanear_red_local():
    logging.info("Iniciando escaneo de red local...")
    dispositivos = []
    red_base = "192.168.1."
    for i in range(1, 255):
        ip = f"{red_base}{i}"
        resultado = subprocess.run(["ping", "-n" if sistema == "Windows" else "-c", "1", ip],
                                   stdout=subprocess.DEVNULL)
        if resultado.returncode == 0:
            dispositivos.append(ip)
    return dispositivos

def escaneo_malware():
    logging.info("Simulando escaneo antivirus IA...")
    # Aquí puedes conectar con tu IA real o análisis ML
    archivos_sospechosos = []
    for root, dirs, files in os.walk("C:\\Users" if sistema == "Windows" else "/home"):
        for file in files:
            if file.lower().endswith(('.exe', '.bat', '.sh', '.py')):
                # Ejemplo: si archivo es sospechoso
                if "mal" in file.lower():
                    archivos_sospechosos.append(os.path.join(root, file))
    return archivos_sospechosos

def bucle_eterno():
    logging.info("Iniciando defensa Totalplay - Usuario: %s", usuario)
    while True:
        if verificar_conexion():
            logging.info("✅ Conexión establecida con Internet")
        else:
            logging.warning("❌ Sin conexión a Internet")

        dispositivos = escanear_red_local()
        logging.info("📡 Dispositivos activos en red: %s", dispositivos)

        amenazas = escaneo_malware()
        if amenazas:
            for archivo in amenazas:
                logging.warning("⚠️ Archivo sospechoso detectado: %s", archivo)

        time.sleep(60)  # Espera 60 segundos entre cada ciclo

# === Ejecutar el sistema ===
if __name__ == "__main__":
    try:
        bucle_eterno()
    except KeyboardInterrupt:
        logging.info("Sistema Totalplay detenido manualmente.")
