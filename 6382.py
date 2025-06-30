import os
import shutil
import hashlib
import datetime
import json

# Ruta de trabajo
PROYECTO = "fgme_proyecto"
HISTORIAL = "fgme_historial/"
INMUTABLE_LOG = "fgme_rollback_log.json"

# Crear carpeta de historial si no existe
os.makedirs(HISTORIAL, exist_ok=True)

# Función para hacer copia inmutable
def hacer_respaldo():
    fecha = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_respaldo = f"{HISTORIAL}respaldo_{fecha}.zip"
    shutil.make_archive(nombre_respaldo.replace(".zip", ""), 'zip', PROYECTO)
    
    # Hash SHA-256 del respaldo
    with open(nombre_respaldo, "rb") as f:
        hash_val = hashlib.sha256(f.read()).hexdigest()
    
    log_respaldo = {
        "fecha": fecha,
        "archivo": nombre_respaldo,
        "hash": hash_val
    }
    
    # Guardar log inmutable
    with open(INMUTABLE_LOG, "a") as log_file:
        log_file.write(json.dumps(log_respaldo) + "\n")
    
    print(f"[✓] Respaldo creado: {nombre_respaldo} | SHA-256: {hash_val}")

# Función para restaurar respaldo
def restaurar_ultimo_respaldo():
    try:
        with open(INMUTABLE_LOG, "r") as log_file:
            entradas = log_file.readlines()
            if not entradas:
                print("[✗] No hay respaldos disponibles.")
                return
            ultimo = json.loads(entradas[-1])
            archivo_zip = ultimo["archivo"]
            
            # Eliminar versión actual
            if os.path.exists(PROYECTO):
                shutil.rmtree(PROYECTO)
            
            # Restaurar respaldo
            shutil.unpack_archive(archivo_zip, PROYECTO)
            print(f"[✓] Restauración completada desde: {archivo_zip}")
    except Exception as e:
        print(f"[✗] Error al restaurar: {e}")

# Bucle automático de respaldo
if __name__ == "__main__":
    while True:
        print("\n[DEFENSA FGME] Escoge opción:")
        print("1. Crear respaldo inmutable")
        print("2. Restaurar último respaldo")
        print("3. Salir")

        op = input("Opción: ")
        if op == "1":
            hacer_respaldo()
        elif op == "2":
            restaurar_ultimo_respaldo()
        elif op == "3":
            break
        else:
            print("Opción no válida.")
