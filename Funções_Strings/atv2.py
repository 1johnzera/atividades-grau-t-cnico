print("Vamos verificar se o número é positivo ou negativo.")

def verificar(numero):
    if numero > 0:
        return "P"
    else:
        return "N"

valor = float(input("Digite um número: "))

resultado = verificar(valor)

print("Resultado:", resultado)