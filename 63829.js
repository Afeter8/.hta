const crypto = require('crypto');
const axios = require('axios');

class RotacionIA {
  constructor(idNodo, intervaloMs = 60000) {
    this.idNodo = idNodo;
    this.intervalo = intervaloMs; // 60 seg
    this.claveActual = null;
    this.historial = [];
    this.nodos = ['http://nodo1.local/api', 'http://nodo2.local/api']; // nodos para sincronizar
  }

  generarClave() {
    // Generar clave aleatoria segura
    return crypto.randomBytes(32).toString('hex');
  }

  async sincronizarConNodos(clave) {
    for (const nodo of this.nodos) {
      try {
        await axios.post(`${nodo}/sincronizar`, { idNodo: this.idNodo, clave });
        console.log(`Clave sincronizada con ${nodo}`);
      } catch (error) {
        console.error(`Error sincronizando con ${nodo}:`, error.message);
      }
    }
  }

  async iniciarBucle() {
    console.log(`Nodo ${this.idNodo} iniciando rotación automática...`);
    setInterval(async () => {
      try {
        this.claveActual = this.generarClave();
        this.historial.push({ clave: this.claveActual, timestamp: new Date() });

        console.log(`Nueva clave generada: ${this.claveActual}`);
        await this.sincronizarConNodos(this.claveActual);

        // Aquí se podría añadir verificación de integridad y reparación

      } catch (error) {
        console.error('Error en bucle de rotación:', error);
      }
    }, this.intervalo);
  }
}

// Ejemplo uso
const rotacion = new RotacionIA('Nodo-FGM-001');
rotacion.iniciarBucle();
