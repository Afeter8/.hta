(function(){
  const arr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split("");
  let i = 0;
  function rotateDom(){
    document.querySelectorAll("body *").forEach(el=>{
      if(el.childNodes[0] && el.childNodes[0].nodeType===3){
        el.childNodes[0].textContent = el.textContent.split("").map(ch=>{
          const idx = arr.indexOf(ch);
          return idx>=0 ? arr[(idx+i)%arr.length] : ch;
        }).join("");
      }
    });
    i=(i+1)%arr.length;
  }
  setInterval(rotateDom, 5000);
})();
