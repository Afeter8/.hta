// Pseudocódigo JS dentro del HTML
function verificarCSS() {
  fetch("StarTigo_Inmutable_Unificado.css")
    .then(res => res.text())
    .then(css => {
      const hash = calcularSHA256(css);
      if (hash !== hashEsperado) alert("⚠️ CSS Alterado");
    });
}
setInterval(verificarCSS, 10000); // Cada 10s
