print("Vamos ler 10 números para cada vetor e criar o vetor C com os elementos intercalados.")

A = []
B = []
C = []

for i in range(10):
    numero = int(input("Digite um número para o vetor A: "))
    A.append(numero)

for i in range(10):
    numero = int(input("Digite um número para o vetor B: "))
    B.append(numero)

for i in range(10):
    C.append(A[i])
    C.append(B[i])

print("Vetor A:", A)
print("Vetor B:", B)
print("Vetor C:", C)