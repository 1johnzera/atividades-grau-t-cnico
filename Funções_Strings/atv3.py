print("Vamos verificar se o número é par ou ímpar.")

def par(numero):
    if numero % 2 == 0:
        return "O número é par"
    else:
        return "O número é ímpar"

valor = int(input("Digite um número inteiro: "))

resultado = par(valor)

print(resultado)