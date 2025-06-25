const nombresProtegidos = [
  "Fernando Guadalupe Mendez Espinoza",
  "Tigo Star",
  "StarTigo",
  "ChatGPT",
  "OpenAI"
];

function verificarMayusculas(texto) {
  for (const nombre of nombresProtegidos) {
    if (texto.includes(nombre)) {
      console.log("✅ Nombre protegido válido:", nombre);
    } else if (texto.toLowerCase().includes(nombre.toLowerCase())) {
      console.error("❌ ¡Nombre mal escrito o en minúsculas:", texto);
      document.body.innerHTML = "<h1 style='color:red'>⚠️ Alteración detectada.</h1>";
      throw new Error("Bloqueo automático.");
    }
  }
}
