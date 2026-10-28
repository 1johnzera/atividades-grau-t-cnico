n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 >= n2 and n1 >= n3:
    maior = n1
    if n2 >= n3:
        meio, menor = n2, n3
    else:
        meio, menor = n3, n2
elif n2 >= n1 and n2 >= n3:
    maior = n2
    if n1 >= n3:
        meio, menor = n1, n3
    else:
        meio, menor = n3, n1
else:
    maior = n3
    if n1 >= n2:
        meio, menor = n1, n2
    else:
        meio, menor = n2, n1

        print("A ordem dos números do maior para o menor é:", maior, meio, menor)
