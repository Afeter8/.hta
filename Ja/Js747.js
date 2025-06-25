async function verificarJsonInmutable() {
  const hashEsperado = "a1b2c3d4e5f6g7h8i9j0"; // Copiado del JSON original

  const response = await fetch('starTigo_inmutable.json');
  const jsonText = await response.text();

  // Simulación de hash simple (puede reemplazarse con SHA-256 real)
  let hash = 0;
  for (let i = 0; i < jsonText.length; i++) {
    hash = ((hash << 5) - hash) + jsonText.charCodeAt(i);
    hash |= 0;
  }
  const hashActual = Math.abs(hash).toString(16);

  if (hashActual !== hashEsperado) {
    document.body.innerHTML = "<h1 style='color:red'>⚠️ JSON alterado o dañado.</h1>";
    throw new Error("JSON inseguro detectado.");
  } else {
    console.log("✅ JSON verificado correctamente.");
  }
}

// 🔁 Bucle eterno cada 10 segundos
setInterval(verificarJsonInmutable, 10000);
