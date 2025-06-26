fetch("totalplay_config.json")
  .then(res => res.json())
  .then(config => {
    if (config.defensa.verificacion_ip) {
      console.log("Verificación IP activada");
    }
    if (config.bucle_eterno) {
      iniciarBucleEterno();
    }
  });
