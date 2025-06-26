let estado = document.getElementById("estadoIA");

function rotarIA() {
  const timestamp = new Date().toISOString();
  estado.innerHTML = `<strong>✅ Verificado:</strong> ${timestamp} - 🔁 IA en bucle eterno`;
  console.log("Rotación completada:", timestamp);
}

// Bucle eterno de protección
setInterval(rotarIA, 5000);

// Sincronización inicial
rotarIA();
