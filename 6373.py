import json

with open('totalplay_config.json', 'r') as f:
    config = json.load(f)

if config['defensa']['escaneo_puertos']:
    print("🔍 Escaneo de puertos activo.")
