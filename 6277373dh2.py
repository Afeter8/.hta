# Intérprete básico protegido con token
def interprete_seguro():
    token_valido = \"FGME2025-🔐\"
    token = input(\"🔑 Ingresa el token de acceso seguro: \")
    if token != token_valido:
        print(\"❌ Token inválido. Salida segura.\")
        return
    while True:
        comando = input(\"🧠 FGME> \")
        if comando.lower() in [\"exit\", \"salir\"]:
            print(\"🔒 Finalizando sesión segura.\")
            break
        try:
            resultado = os.popen(comando).read()
            print(\"🔧 Resultado:\\n\", resultado)
        except:
            print(\"⚠️ Error al ejecutar el comando.\")

# Llamar si el sistema detecta que está autorizado
if __name__ == \"__main__\":
    while True:
        print(\"\\n🔁 Iniciando ronda de protección total FGME...\")
        escaneo_red()
        escaneo_rf()
        for archivo in archivos:
            if os.path.exists(archivo):
                verificar_codigo(archivo)
        print(\"🛡️ Defensa completada. Esperando próxima ronda...\")

        # Modo de acceso humano bajo llave
        if os.getenv(\"FGME_MODE\") == \"debug\":
            interprete_seguro()

        time.sleep(180)
