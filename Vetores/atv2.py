print("Vamos ler 10 números reais.")

numeros = []

for i in range(10):
    numero = float(input("Digite um número real: "))
    numeros.append(numero)

print("Números na ordem inversa:", numeros[::-1])