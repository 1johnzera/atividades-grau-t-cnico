print("Vamos listar e somar os números entre dois números digitados.")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = 0

for numero in range(min(numero1, numero2) + 1, max(numero1, numero2)):
    print(numero)
    soma += numero

print("A soma dos números é:", soma)
