import random

with open("animais.txt", "r") as arquivo:
    lista_animais = arquivo.readlines()
animal_sorteado = random.choice(lista_animais).strip()
print(f"Animal sorteado: {animal_sorteado}")
