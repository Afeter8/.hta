// === Sistema Inmutable.js para Defensa IA ===
// Autor: Star Tigo IA – Fernando Guadalupe Mendez Espinoza
// Protección automática, rotación y vigilancia en bucle eterno

(function startInmutableDefense() {
  const ROTACION_INTERVALO_MS = 5000;

  const caracteresProtegidos = [
    ..."ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    ..."abcdefghijklmnopqrstuvwxyz",
    ..."0123456789",
    ..."!@#$%^&*()-_=+[]{}|;:',.<>/?`~",
    "🌐", "🔐", "💾", "🛡️", "🧠", "♻️"
  ];

  function rotarCadena(str) {
    return str
      .split('')
      .map(char => {
        const index = caracteresProtegidos.indexOf(char);
        return index !== -1
          ? caracteresProtegidos[(index + 1) % caracteresProtegidos.length]
          : char;
      })
      .join('');
  }

  function escanearYRotar() {
    const elementos = document.querySelectorAll("*");

    elementos.forEach(el => {
      if (el.childNodes.length) {
        el.childNodes.forEach(node => {
          if (node.nodeType === 3 && node.textContent.trim() !== "") {
            node.textContent = rotarCadena(node.textContent);
          }
        });
      }
    });

    console.log("🛡️ Defensa IA: Rotación aplicada con éxito.");
  }

  function vigilanciaEterna() {
    escanearYRotar();
    setTimeout(vigilanciaEterna, ROTACION_INTERVALO_MS);
  }

  function inicializarSistema() {
    console.log("🧠 Sistema Inmutable.js activado");
    vigilanciaEterna();
  }

  inicializarSistema();
})();
