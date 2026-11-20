print("Vamos contar as vogais da palavra.")

def contar_vogais(palavra):
    quantidade = 0

    for letra in palavra:
        if letra in "aeiou":
            quantidade = quantidade + 1

    return quantidade

palavra = input("Digite uma palavra: ").lower()

resultado = contar_vogais(palavra)

print("Palavra:", palavra)
print("Quantidade de vogais:", resultado)