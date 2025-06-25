setInterval(() => {
  fetch("wallet_protegida.json")
    .then(r => r.text())
    .then(data => {
      if (!data.includes("Fernando") || !data.includes("IA Inmutable")) {
        document.body.innerHTML = "<h1>🚫 Bloqueado por IA CESAR</h1>";
        throw new Error("Sistema violado");
      }
    });
}, 5000);
