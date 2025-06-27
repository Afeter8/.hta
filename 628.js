detectarAmenazas: function() {
  // Detectar iframes maliciosos
  const enFrame = window.self !== window.top;
  
  // Detectar visibilidad de la página
  const oculto = document.hidden;
  
  // Detectar automatización (Selenium, etc.)
  const automation = navigator.webdriver;
  
  // Detectar herramientas de desarrollo
  const devTools = window.outerWidth - window.innerWidth > 100;
  
  return enFrame || oculto || automation || devTools;
}
