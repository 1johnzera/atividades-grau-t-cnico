print("Vamos calcular a potência de um número digitado.")

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

for i in range(expoente):
    resultado *= base

print("O resultado é:", resultado)
