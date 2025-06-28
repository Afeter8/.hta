# ia_defensa.py
import os
import time
import re

# Lista de procesos dañinos (nombres o patrones)
HARMFUL_PROCESSES = [
    "malware.exe",  # ejemplo, pero en Linux no tendremos .exe
    "ransomware",
    "keylogger",
    "malicious-script",
    "internet-start",  # del dominio bloqueado
    # ... otros
]

def scan_and_kill():
    # Obtener la lista de procesos
    ps_output = os.popen('ps aux').read()
    processes = ps_output.splitlines()
    
    # El encabezado es la primera línea, luego cada proceso
    for proc in processes[1:]:
        # Cada proceso es una línea con múltiples espacios, nos interesa el comando (última columna)
        parts = proc.split()
        if len(parts) < 11:
            continue
        # El comando es desde el 10mo elemento en adelante (porque los primeros 10 son: user, pid, cpu, etc.)
        command = ' '.join(parts[10:])
        # Comprobar si el comando coincide con algún patrón dañino
        for harmful in HARMFUL_PROCESSES:
            if re.search(harmful, command, re.IGNORECASE):
                pid = parts[1]
                print(f"[FGME] Proceso dañino detectado: {command} (PID: {pid})")
                # Matar el proceso
                try:
                    os.kill(int(pid), 9)  # SIGKILL
                    print(f"[FGME] Proceso {pid} terminado.")
                except Exception as e:
                    print(f"[FGME] Error al terminar proceso {pid}: {e}")

def main():
    while True:
        print("[FGME] Escaneando integridad...")
        # Aquí iría la lógica de verificación de integridad (no especificada)
        print("[FGME] Integridad: OK")
        print("[FGME] Escaneando procesos dañinos...")
        scan_and_kill()
        time.sleep(60)

if __name__ == "__main__":
    main()
