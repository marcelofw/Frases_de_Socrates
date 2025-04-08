import random

with open("C:\Python\Frases_de_Socrates\socrates.txt", "r", encoding="utf-8") as arquivo:
    frases = arquivo.readlines()

frase_escolhida = random.choice(frases)

print(frase_escolhida)


