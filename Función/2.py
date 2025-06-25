import json, os

def cargar_region(pais):
    with open("datasets/data_regional.json") as f:
        return json.load(f)[pais]

def fusionar_codigo(pais):
    config = cargar_region(pais)
    fusion = ""

    for archivo in os.listdir("base_code"):
        with open(f"base_code/{archivo}", "r", encoding="utf-8") as f:
            fusion += f"\n<!-- {archivo} → Región: {pais} -->\n{f.read()}"

    # Inyección de emojis culturales y estilo regional
    fusion += "\n<!-- Emojis culturales -->\n"
    fusion += " ".join(config["emojis"])

    with open(f"codex_por_pais/codex_{pais.lower()}.fer", "w", encoding="utf-8") as f:
        f.write(fusion)

for pais in ["México", "Japón", "Brasil"]:
    fusionar_codigo(pais)
