while True:
    monitorear_trafico()
    if detectar_intrusion():
        activar_defensas()
        loggear_intento("Fernando GME")
        bloquear_IP()
        notificar_a_sistema()
