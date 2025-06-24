import serial
import time

def obtener_datos_gps():
    puerto = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
    while True:
        linea = puerto.readline().decode("utf-8", errors="ignore")
        if "$GPGGA" in linea:
            print("Datos GPS:", linea.strip())
            # Aquí puedes agregar la verificación o envío a servidor
        time.sleep(1)

obtener_datos_gps()
