print("Vamos calcular o menor valor, o maior valor e a soma dos números digitados.")

n = int(input("Quantos números deseja informar? "))

menor = None
maior = None
soma = 0

for i in range(n):
    numero = float(input(f"Digite o {i+1}º número: "))

    if menor is None or numero < menor:
        menor = numero

    if maior is None or numero > maior:
        maior = numero

    soma += numero

print("Menor valor:", menor)
print("Maior valor:", maior)
print("Soma dos valores:", soma)
