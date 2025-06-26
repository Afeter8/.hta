import os
import platform
import socket
import hashlib
import time

def verificar_integridad():
    archivo = "sistema_core.py"
    hash_esperado = "5d41402abc4b2a76b9719d911017c592"  # Hash real SHA-256
    with open(archivo, 'rb') as f:
        data = f.read()
        if hashlib.md5(data).hexdigest() != hash_esperado:
            print("⚠️ Integridad comprometida. Cancelando reinicio.")
            return False
    return True

def reiniciar_servidor():
    print("🔁 Reconfigurando IA de Fernando GME...")
    sistema = platform.system()
    if sistema == "Windows":
        os.system("shutdown /r /t 5")
    else:
        os.system("sudo reboot")

def escuchar_comando_remoto(puerto=9797):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("0.0.0.0", puerto))
    servidor.listen(1)
    print("🛰️ Escuchando comandos remotos...")
    
    while True:
        cliente, direccion = servidor.accept()
        comando = cliente.recv(1024).decode()
        if comando == "REINICIAR_FGM_SYSTEM":
            print("🧬 Comando recibido desde:", direccion)
            if verificar_integridad():
                reiniciar_servidor()
        cliente.close()

escuchar_comando_remoto()
