import time

paises = ["México", "Japón", "India", "Alemania"]

while True:
    for pais in paises:
        os.system(f"python3 combinador_global.py {pais}")
    time.sleep(3600)  # Ejecutar cada hora
