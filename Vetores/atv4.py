print("Vamos ver quantas consoantes foram digitadas.")

letras = []
consoantes = []

for i in range(10):
    letra = input("Digite uma letra: ").lower()
    letras.append(letra)

    if letra not in "aeiou":
        consoantes.append(letra)

print("Quantidade de consoantes:", len(consoantes))
print("Consoantes digitadas:", consoantes)