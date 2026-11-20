print("Vamos ler 5 números e calcular a soma e a multiplicação.")

numeros = []
soma = 0
multiplicacao = 1

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

    soma = soma + numero
    multiplicacao = multiplicacao * numero

print("Números digitados:", numeros)
print("Soma:", soma)
print("Multiplicação:", multiplicacao)