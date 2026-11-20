print("Vamos calcular o fatorial de um número.")
print("Lembre-se: o fatorial de um número n é o produto de todos os números inteiros positivos menores ou iguais a n.")

def fatorial(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado = resultado * i

    return resultado

numero = int(input("Digite um número inteiro: "))

resultado = fatorial(numero)

print("Fatorial:", resultado)