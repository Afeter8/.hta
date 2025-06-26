import time
import random

# Configuración tipo JSON para los proveedores de internet
config = {
    "proveedores": [
        {"nombre": "Telmex", "pais": "México", "region": "Centro", "idioma": "es", "tipoConexion": ["Fibra óptica", "ADSL", "Cable"], "prioridad": 1},
        {"nombre": "Megacable", "pais": "México", "region": "Occidente", "idioma": "es", "tipoConexion": ["Cable", "Fibra óptica"], "prioridad": 2},
        {"nombre": "izzi", "pais": "México", "region": "Centro-Sur", "idioma": "es", "tipoConexion": ["Cable", "Fibra óptica"], "prioridad": 3},
        {"nombre": "Totalplay", "pais": "México", "region": "Nacional", "idioma": "es", "tipoConexion": ["Fibra óptica"], "prioridad": 4},
        {"nombre": "Skay", "pais": "Latinoamérica", "region": "Sur", "idioma": "es", "tipoConexion": ["Satélite"], "prioridad": 5},
        {"nombre": "Starlink", "pais": "Global", "region": "Global", "idioma": "multi", "tipoConexion": ["Satélite"], "prioridad": 6},
        {"nombre": "CFE Internet", "pais": "México", "region": "Rural", "idioma": "es", "tipoConexion": ["Fibra óptica", "ADSL"], "prioridad": 7},
        {"nombre": "Blutelecom", "pais": "México", "region": "Norte", "idioma": "es", "tipoConexion": ["Cable", "Fibra óptica"], "prioridad": 8},
        {"nombre": "Axel", "pais": "México", "region": "Desconocido", "idioma": "es", "tipoConexion": ["ADSL"], "prioridad": 9},
        {"nombre": "Telefónica", "pais": "España", "region": "Europa", "idioma": "es", "tipoConexion": ["Fibra óptica", "ADSL", "Cable"], "prioridad": 10}
    ],
    "parametrosRotacion": {
        "intervaloSegundos": 10,
        "maxIntentos": 3,
        "estrategia": "rotativo",
        "fallbackHabilitado": True
    }
}

class ConexionInternet:
    def __init__(self, config):
        self.proveedores = sorted(config["proveedores"], key=lambda p: p["prioridad"])
        self.intervalo = config["parametrosRotacion"]["intervaloSegundos"]
        self.max_intentos = config["parametrosRotacion"]["maxIntentos"]
        self.fallback = config["parametrosRotacion"]["fallbackHabilitado"]
        self.indice_actual = 0

    def conectar(self, proveedor):
        """
        Simula intentar conectarse a un proveedor de internet.
        En un sistema real, aquí irían las llamadas a la API o comandos de sistema.
        Retorna True si la conexión fue exitosa, False si no.
        """
        print(f"Intentando conexión con proveedor: {proveedor['nombre']} ({proveedor['pais']} - {proveedor['region']})...")
        # Simulación de éxito aleatorio basado en prioridad (para ejemplo)
        prob_exito = 0.7 - (proveedor["prioridad"] * 0.05)  # Proveedores con menor prioridad son menos confiables
        exito = random.random() < prob_exito
        time.sleep(2)  # Simular tiempo conexión
        if exito:
            print(f"Conectado exitosamente a {proveedor['nombre']}!")
            return True
        else:
            print(f"Fallo al conectar con {proveedor['nombre']}.")
            return False

    def rotacion(self):
        """
        Realiza la rotación en bucle eterno según configuración.
        """
        while True:
            proveedor = self.proveedores[self.indice_actual]
            intentos = 0
            conectado = False

            while intentos < self.max_intentos and not conectado:
                conectado = self.conectar(proveedor)
                intentos += 1
                if not conectado:
                    print(f"Reintentando ({intentos}/{self.max_intentos}) en {self.intervalo} segundos...")
                    time.sleep(self.intervalo)

            if conectado:
                print(f"Manteniendo conexión con {proveedor['nombre']} por {self.intervalo} segundos.")
                time.sleep(self.intervalo)
            else:
                print(f"No se pudo conectar a {proveedor['nombre']} después de {self.max_intentos} intentos.")

                if self.fallback:
                    print("Intentando fallback al siguiente proveedor...")
                    self.indice_actual = (self.indice_actual + 1) % len(self.proveedores)
                    continue
                else:
                    print("Fallback deshabilitado, esperando antes de reintentar...")
                    time.sleep(self.intervalo)

            # Avanzar al siguiente proveedor
            self.indice_actual = (self.indice_actual + 1) % len(self.proveedores)

if __name__ == "__main__":
    conexion = ConexionInternet(config)
    conexion.rotacion()
