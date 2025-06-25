import hashlib

def hash_archivo(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

for archivo in os.listdir("codex_por_pais"):
    print(f"{archivo}: {hash_archivo(f'codex_por_pais/{archivo}')}")
