actualizarDesdeRepositorios: function() {
  this.repositorios.forEach(repo => {
    console.log(`[FGME] 🔄 Verificando: ${repo}`);
    // En implementación real se haría:
    // fetch(`${repo}/version-actual`)
    // .then(response => compararVersiones())
    // .then(actualizarSiEsNecesario)
  });
}
