print("Vamos calcular a soma e a média de 5 números digitados.")

soma = 0

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero 

media = soma / 5

print("A soma dos números é:", soma)
print("A média dos números é:", media)
