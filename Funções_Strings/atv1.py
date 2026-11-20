print("Vamos somar três números.")

def somar(a, b, c):
    return a + b + c

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

resultado = somar(n1, n2, n3)

print("A soma dos números é:", resultado)