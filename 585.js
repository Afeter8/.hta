// inmutable.js
setInterval(() => {
    const fecha = new Date();
    const claveRotativa = btoa(`${fecha.getFullYear()}-${fecha.getMonth()}-${fecha.getDate()}`);
    localStorage.setItem("clave_rotativa", claveRotativa);
    // Usa esta clave para cifrar/desencriptar el código
}, 60000); // Cada minuto
