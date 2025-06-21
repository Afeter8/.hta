# Publicar automáticamente cambios a múltiples redes
import subprocess

def push_to_radicle():
    subprocess.run("git push radicle@seed.node:project.git", shell=True)

def push_to_ipfs():
    subprocess.run("git-remote-ipfs push origin master", shell=True)

def push_to_arweave():
    subprocess.run("arweave deploy ./codigo/", shell=True)

def bucle_autopush():
    while True:
        push_to_radicle()
        push_to_ipfs()
        push_to_arweave()
