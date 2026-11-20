print("Vamos gerar a sequência de Fibonacci.")

n = int(input("Quantos termos da sequência deseja gerar? "))

a = 1
b = 1

for i in range(n):
    print(a)
    proximo = a + b
    a = b
    b = proximo
