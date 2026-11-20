print("Vamos calcular o fatorial de um número digitado.")

numero = int(input("Digite um número inteiro: "))

fatorial = 1

for i in range(numero, 0, -1):
    fatorial *= i

print("O fatorial de", numero, "é:", fatorial)
