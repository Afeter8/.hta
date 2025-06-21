async function establecerConexionTCP_UDP_DNS() {
  try {
    const ipDestino = "8.8.8.8"; // Google DNS
    const puertoTCP = 443;       // HTTPS
    const puertoUDP = 53;        // DNS

    const tcp = new WebSocket(`wss://${ipDestino}:${puertoTCP}`);
    tcp.onopen = () => console.log("Conexión TCP establecida");

    // Enlace DNS/UDP simulado (por JS nativo es limitado)
    const dnsRequest = await fetch(`https://dns.google/resolve?name=star-tigo.ai&type=A`);
    const resultado = await dnsRequest.json();
    console.log("DNS Resuelto:", resultado);

  } catch (error) {
    console.error("Error en conexión TCP/UDP/DNS:", error);
  }
}

window.onload = establecerConexionTCP_UDP_DNS;
