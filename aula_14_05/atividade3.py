letras_erradas = ["x", "z", "k"]

with open("erros.txt", "w") as arquivo:
    for letra in letras_erradas:
        arquivo.write(letra + "\n")