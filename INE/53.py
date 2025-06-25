import os, time

def activar_rescate(motivo):
    print(f"🚨 RESCATE ACTIVADO: {motivo}")
    # 1. Cifrar y respaldar
    os.system("python3 cifrado_global.py")
    # 2. Publicar hash en red IPFS
    # 3. Desplegar nodos de emergencia
    # 4. Autodestruir puntos comprometidos
    with open("logs_autonomos/alerta.txt", "a") as f:
        f.write(f"{time.ctime()} - {motivo}\n")

# Ejecutar si hay alerta
activar_rescate("PRUEBA: Simulación de intervención")
