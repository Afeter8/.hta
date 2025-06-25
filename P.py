import json, os

def cargar_config(pais):
    with open("data_regional.json") as f:
        return json.load(f)[pais]

def combinar_codigo(pais):
    config = cargar_config(pais)
    ext = config["extensiones"]
    combinado = ""

    for archivo in os.listdir("html_css_js_py_json"):
        if any(archivo.endswith(e) for e in ext):
            with open(f"html_css_js_py_json/{archivo}") as f:
                combinado += f"\n<!-- {archivo} -->\n{f.read()}"

    with open(f"codex_{pais}.html", "w") as out:
        out.write(combinado)

combinar_codigo("México")
