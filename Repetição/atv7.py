print("Vamos listar os números entre dois números digitados.")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

for numero in range(numero1 + 1, numero2):
    print(numero)
