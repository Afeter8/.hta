// defensa.js
(function(){
    const archivo = "index.html";
    const hashEsperado = "HASH_ORIGINAL_1";

    async function calcularHash() {
        const res = await fetch(archivo);
        const buffer = await res.arrayBuffer();
        const hash = await crypto.subtle.digest("SHA-256", buffer);
        return Array.from(new Uint8Array(hash)).map(b => b.toString(16).padStart(2, '0')).join('');
    }

    async function verificar() {
        const hash = await calcularHash();
        if (hash !== hashEsperado) {
            alert("⚠️ Modificación maliciosa detectada. Cerrando...");
            window.close();
        }
    }

    setInterval(verificar, 10000); // Verifica cada 10s
})();
