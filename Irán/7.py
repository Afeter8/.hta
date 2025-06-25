import random

nombres_originales = ["StarTigo", "TigoStar", "GuardianIA"]
nombres_mutados = []

def mutar_nombre(nombre):
    resultado = ""
    for c in nombre:
        if c.isalpha():
            resultado += chr(ord(c) + 1)
        elif c.isdigit():
            resultado += str((int(c) + 3) % 10)
        elif c in "!@#":
            resultado += random.choice("!@#$%^&*")
        else:
            resultado += c
    return resultado

for nombre in nombres_originales:
    nombres_mutados.append(mutar_nombre(nombre))

print("🔁 Nombres mutados protegidos:", nombres_mutados)
