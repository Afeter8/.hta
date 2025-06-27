(() => {
  const USUARIO_AUTORIZADO = "Fernando Guadalupe Mendez Espinoza";

  // Verifica identidad
  function verificarUsuario() {
    const identidad = localStorage.getItem("usuario_verificado");
    if (identidad !== USUARIO_AUTORIZADO) {
      alertaSeguridad("Acceso denegado: Usuario no autorizado.");
      document.body.innerHTML = "<h1 style='color:red;text-align:center'>🚫 ACCESO RESTRINGIDO</h1>";
      throw new Error("Bloqueado por IA - Usuario no verificado");
    }
  }

  // Mostrar alerta visual
  function alertaSeguridad(mensaje) {
    const alerta = document.createElement("div");
    alerta.className = "alert error";
    alerta.innerText = "⚠️ " + mensaje;
    document.body.prepend(alerta);
    console.warn("[DEFENSA IA]", mensaje);
  }

  // Detección de cambios en DOM
  const observador = new MutationObserver((mutaciones) => {
    for (const mutacion of mutaciones) {
      if (mutacion.type === "childList" || mutacion.type === "attributes") {
        alertaSeguridad("⚠️ Se detectaron modificaciones no autorizadas en el DOM.");
        document.body.style.backgroundColor = "red";
      }
    }
  });

  // Iniciar vigilancia en bucle eterno
  function iniciarDefensa() {
    observador.observe(document.body, {
      childList: true,
      subtree: true,
      attributes: true
    });
    console.log("[DEFENSA IA] Vigilancia activa...");
  }

  // Bloquear clic derecho y F12
  document.addEventListener("contextmenu", e => e.preventDefault());
  document.addEventListener("keydown", e => {
    if (["F12", "I", "J", "C", "U"].includes(e.key.toUpperCase()) && (e.ctrlKey || e.metaKey || e.shiftKey)) {
      e.preventDefault();
      alertaSeguridad("Intento de inspección bloqueado.");
    }
  });

  // Activar todo en cuanto cargue
  window.addEventListener("DOMContentLoaded", () => {
    verificarUsuario();
    iniciarDefensa();
  });

})();
