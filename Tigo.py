def validar_usuario():
    if validar_huella() and validar_rostro() and validar_voz():
        return True
    else:
        bloquear_acceso()

# Ejecución automática IA
def ejecutar_solo_si_autorizado():
    if validar_usuario():
        iniciar_proyecto_star_tigo()
    else:
        registrar_intento_y_autodestruir()
