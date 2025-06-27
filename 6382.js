repararSistema: function() {
  // Restaurar elementos críticos faltantes
  if(!document.getElementById('quantum-shield')) {
    const shield = document.createElement('div');
    shield.id = 'quantum-shield';
    shield.className = 'quantum-shield';
    document.body.appendChild(shield);
  }
  
  // Restaurar marca de agua de copyright
  if(!document.getElementById('copyright-watermark')) {
    const watermark = document.createElement('div');
    watermark.id = 'copyright-watermark';
    watermark.className = 'copyright-watermark';
    watermark.textContent = `© ${new Date().getFullYear()} ${this.propietario} - STAR TIGO`;
    document.body.appendChild(watermark);
  }
}
