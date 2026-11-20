print("Vamos ler 10 números e calcular a soma dos quadrados.")

A = []
soma = 0

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    A.append(numero)

    soma = soma + numero ** 2

print("Números digitados:", A)
print("Soma dos quadrados:", soma)