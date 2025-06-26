// Defensa IA en navegador
setInterval(() => {
  fetch("https://api.ipify.org?format=json")
    .then(r => r.json())
    .then(data => {
      console.log("IP detectada:", data.ip);
    });
}, 30000); // Cada 30 seg
