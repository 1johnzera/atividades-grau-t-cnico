print("Vamos ler 20 números e dizer quais são pares e quais são ímpares.")

numeros = []
PAR = []
IMPAR = []

for i in range(20):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

    if numero % 2 == 0:
        PAR.append(numero)
    else:
        IMPAR.append(numero)

print("Todos os números:", numeros)
print("Números pares:", PAR)
print("Números ímpares:", IMPAR)