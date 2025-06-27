import time
import hashlib
import sys

# Símbolo especial secreto
SIMBOLO_BLOQUEO = "��"

# Usuario autorizado
USUARIO_AUTORIZADO = "Fernando Guadalupe Mendez Espinoza"

# Validación de acceso con símbolo especial
def validar_acceso(entrada_usuario):
    hash_simbolo = hashlib.sha256(SIMBOLO_BLOQUEO.encode()).hexdigest()
    entrada_hash = hashlib.sha256(entrada_usuario.encode()).hexdigest()
    return entrada_hash == hash_simbolo

# Bucle eterno de protección
def sistema_bloqueo():
    print("[🔐] Sistema IA de bloqueo activado en modo inmutable.")
    while True:
        try:
            entrada = input("⚠️ Ingrese código de seguridad IA: ")
            if validar_acceso(entrada):
                print(f"[✅] Bienvenido, {USUARIO_AUTORIZADO}. Acceso autorizado.")
            else:
                print("[⛔] Acceso denegado. Sistema bloqueado por IA.")
                time.sleep(1)
                bloquear_sistema()
        except KeyboardInterrupt:
            print("\n[🛑] Intervención detectada. Reiniciando protección.")
            time.sleep(1)

# Acción de bloqueo fuerte
def bloquear_sistema():
    print("[🚨] Código inválido. Cerrando terminal y activando escudo inmutable.")
    time.sleep(2)
    sys.exit(1)

# Inicio del sistema
if __name__ == "__main__":
    sistema_bloqueo()
