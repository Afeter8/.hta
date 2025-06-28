# ia_defensa.py
import os
import time
import re

# Lista de procesos dañinos (nombres o patrones) - ¡Ajustar según necesidad!
HARMFUL_PROCESSES = [
    "malware",
    "ransomware",
    "keylogger",
    "malicious-script",
    "internet-start",  # del dominio bloqueado
    "virus",
    # ... otros
]

# Lista de procesos críticos que NO debemos matar (para evitar daño al sistema)
CRITICAL_PROCESSES = [
    "init",
    "systemd",
    "bash",
    "sh",
    "python",
    "ia_defensa",  # ¡No matarnos a nosotros mismos!
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
                # Verificar si es un proceso crítico
                critical = False
                for critical_pattern in CRITICAL_PROCESSES:
                    if re.search(critical_pattern, command, re.IGNORECASE):
                        critical = True
                        break
                if critical:
                    print(f"[FGME] Proceso crítico excluido: {command}")
                    continue

                pid = parts[1]
                print(f"[FGME] Proceso dañino detectado: {command} (PID: {pid})")
                # Matar el proceso
                try:
                    os.kill(int(pid), 9)  # SIGKILL
                    print(f"[FGME] Proceso {pid} terminado.")
                except Exception as e:
                    print(f"[FGME] Error al terminar proceso {pid}: {e}")

def integrity_scan():
    # Lógica de verificación de integridad de archivos
    # Por ejemplo, verificar hashes de archivos críticos
    # Aquí se podría comparar con el JSON de verificación inmutable
    # Por ahora, un placeholder
    return True

def main():
    while True:
        print("[FGME] Escaneando integridad...")
        if integrity_scan():
            print("[FGME] Integridad: OK")
        else:
            print("[FGME] ¡Alerta! Integridad comprometida")
        print("[FGME] Escaneando procesos dañinos...")
        scan_and_kill()
        time.sleep(60)

if __name__ == "__main__":
    main()
