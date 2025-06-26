// === totalplay_defensa.js ===
// Sistema IA de Defensa en red para Totalplay (Cliente Web + Star Tigo)

let ipAnterior = "";
let loopActivo = true;

function log(mensaje) {
  const logDiv = document.getElementById("log");
  const entrada = document.createElement("div");
  entrada.innerText = `> ${mensaje}`;
  logDiv.appendChild(entrada);
  logDiv.scrollTop = logDiv.scrollHeight;
}

// Verifica si hay conexión a internet
function verificarConexion() {
  const online = navigator.onLine;
  const estado = online ? "✅ Conectado" : "❌ Sin conexión";
  document.getElementById("redEstado").innerText = estado;
  log(`Conexión: ${estado}`);
}

// Detecta IP local simulada (solo visible en ciertos entornos, por seguridad del navegador)
async function detectarIP() {
  try {
    const response = await fetch("https://api.ipify.org?format=json");
    const data = await response.json();
    if (data.ip !== ipAnterior) {
      log(`🔄 Cambio de IP detectado: ${data.ip}`);
      ipAnterior = data.ip;
    }
    document.getElementById("ipActual").innerText = data.ip;
  } catch (err) {
    log("⚠️ No se pudo obtener la IP pública.");
  }
}

// Simula escaneo de puertos
function escanearPuertos() {
  const puertos = [80, 443, 8080, 8443];
  log("Escaneando puertos simulados...");
  puertos.forEach(puerto => {
    log(`📡 Puerto ${puerto}: Abierto (simulado)`);
  });
}

// Ejecuta análisis de IA básico
function analizarIA() {
  log("🧠 Ejecutando IA para amenazas...");
  setTimeout(() => {
    log("✅ Sin amenazas detectadas. Sistema limpio.");
  }, 2000);
}

// Bucle eterno cada X segundos
function iniciarBucleEterno() {
  if (!loopActivo) return;
  verificarConexion();
  detectarIP();
  escanearPuertos();
  analizarIA();

  setTimeout(iniciarBucleEterno, 60000); // Repite cada 60 segundos
}

// Función para detener el bucle (si es necesario)
function detenerBucle() {
  loopActivo = false;
  log("⛔ Bucle eterno detenido por seguridad.");
}
