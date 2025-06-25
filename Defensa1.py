from github import Github
import os

def verificar_proyectos():
    g = Github("TOKEN_DE_GITHUB")
    user = g.get_user("FernandoGMendez")
    repos = user.get_repos()
    for repo in repos:
        print(f"🔒 Protegiendo {repo.name}")
        if repo.private:
            print("✅ Privado OK")
        else:
            repo.edit(private=True)
            print("🔐 Convertido a privado")

verificar_proyectos()
