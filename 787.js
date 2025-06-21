fetch("reparacion_inmutable.json")
  .then(res => res.json())
  .then(data => {
    data.reparaciones.forEach(rep => {
      if (rep.inmutable && rep.estado !== "ok") {
        console.log(`🔧 Reparando ${rep.nombre} con IA: ${rep.ia_asociada}`);
        // Ejecutar lógica específica o notificar al backend
      }
    });
  });
