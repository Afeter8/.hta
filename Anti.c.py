def analizar_censura(texto, pais):
    palabras_prohibidas = {
        "CN": ["democracia", "libertad"],
        "IR": ["mujer", "derechos"],
        "RU": ["protesta", "oposición"]
    }
    if pais in palabras_prohibidas:
        for palabra in palabras_prohibidas[pais]:
            if palabra in texto:
                return f"⚠️ Intento de censura detectado: {palabra}"
    return "🟢 Sin censura"

print(analizar_censura("viva la democracia", "CN"))
