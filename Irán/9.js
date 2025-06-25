const componentesProtegidos = ["StarTigo", "🌐", "🔐", "IA", "GPT", "🧠"];
setInterval(() => {
  let html = document.body.innerText;
  componentesProtegidos.forEach(comp => {
    if (!html.includes(comp)) {
      window.location.href = "honeypot.html";
    }
  });
}, 10000);
