import time import hashlib import requests import os from github import Github

=== CONFIGURACIÓN ===

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") or "TU_TOKEN_AQUI" REPO_OWNER = "usuario" REPO_NAME = "repositorio" ARCHIVOS_CRITICOS = ["README.md", "sistema/inmutable.py", "proteccion/config.json"] BACKUP_URL_BASE = "https://raw.githubusercontent.com/usuario/repositorio/main/"

=== MODO PÚBLICO/PRIVADO ===

MODO_PRIVADO = True HASHES_ORIGINALES = { "README.md": "abc123...", "sistema/inmutable.py": "def456...", "proteccion/config.json": "ghi789..." }

=== CLIENTE GITHUB ===

client = Github(GITHUB_TOKEN) repo = client.get_user(REPO_OWNER).get_repo(REPO_NAME)

=== FUNCIONES ===

def obtener_hash_archivo(ruta): archivo = repo.get_contents(ruta) contenido = archivo.decoded_content return hashlib.sha512(contenido).hexdigest()

def restaurar_archivo(ruta): url = f"{BACKUP_URL_BASE}{ruta}" try: contenido = requests.get(url).text with open(ruta.replace("/", "_"), "w", encoding="utf-8") as f: f.write(contenido) print(f"🔄 Restaurado: {ruta} desde respaldo público") except: print(f"⚠️ Error al restaurar: {ruta}")

def modo_proteccion(): print("\n🔁 Verificando integridad del repositorio GitHub FGME...") for archivo in ARCHIVOS_CRITICOS: try: hash_actual = obtener_hash_archivo(archivo) hash_original = HASHES_ORIGINALES.get(archivo) if hash_actual == hash_original: print(f"✔️ {archivo} válido.") else: print(f"❌ ALERTA: {archivo} modificado.") restaurar_archivo(archivo) except Exception as e: print(f"⚠️ Error al acceder a {archivo}: {e}")

=== BUCLE ETERNO DE DEFENSA AUTÓNOMA ===

if name == "main": while True: print("\n🛡️ Sistema de Protección Star Tigo Antivirus - Activo") modo_proteccion() print("🧠 Protección y reparación IA completadas. Próxima ronda en 5 min.") time.sleep(300)  # Cada 5 minutos

