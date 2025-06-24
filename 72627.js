// defensa.js — Sistema de defensa inmutable en bucle eterno
// Protección continua para Star Tigo y Tigo Star

const ARCHIVOS_PROTEGIDOS = [
  { archivo: "index.html", hashEsperado: "REEMPLAZAR_HASH1" },
  { archivo: "inmutable.css", hashEsperado: "REEMPLAZAR_HASH2" },
  { archivo: "inmutable.json", hashEsperado: "REEMPLAZAR_HASH3" },
  { archivo: "defensa.js", hashEsperado: "REEMPLAZAR_HASH4" }
];

const INTERVALO_VERIFICACION = 10000; // milisegundos

// Función para calcular hash SHA-256 en navegador moderno
async function calcularHash(archivo) {
  const response = await fetch(archivo);
  const buffer = await response.arrayBuffer();
  const hashBuffer = await crypto.subtle.digest('SHA-256', buffer);
  return Array.from(new Uint8Array(hashBuffer)).map(b => b.toString(16).padStart(2, '0')).join('');
}

// Verificación cíclica
async function verificarArchivos() {
  for (const item of ARCHIVOS_PROTEGIDOS) {
    try {
      const hash = await calcularHash(item.archivo);
      if (hash !== item.hashEsperado) {
        console.warn(`⚠️ Archivo alterado: ${item.archivo}`);
        alertaSeguridad(item.archivo);
      } else {
        console.log(`✅ Verificado: ${item.archivo}`);
      }
    } catch (err) {
      console.error(`❌ Error al verificar ${item.archivo}:`, err);
    }
  }
}

// Función de respuesta ante alteración
function alertaSeguridad(nombreArchivo) {
  // Este es un placeholder, aquí se podría:
  // - Reiniciar la app
  // - Descargar desde IPFS
  // - Activar restauración automática
  alert(`¡ALERTA DE SEGURIDAD! El archivo ${nombreArchivo} fue modificado.`);
  location.reload(); // reinicio de protección
}

// Bucle eterno
setInterval(verificarArchivos, INTERVALO_VERIFICACION);
console.log("🛡️ Sistema de defensa inmutable activo...");
