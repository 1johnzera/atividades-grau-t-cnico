
print("Vamos encontrar o maior número entre 5 números digitados.")

numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior = max(numeros)

print("O maior número é:", maior)
