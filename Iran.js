setInterval(() => {
  fetch("json_config.json")
    .then(r => r.json())
    .then(json => {
      const hashActual = JSON.stringify(json).length.toString(16); // simulación
      if (json.hash_sha256 !== hashActual) {
        document.body.innerHTML = "<h1 style='color:red'>⚠️ Sistema Alterado</h1>";
        throw new Error("Archivo JSON modificado.");
      }
    });
}, 10000);
