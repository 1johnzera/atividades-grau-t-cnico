n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 >= n2 and n1 >= n3:
    print("O maior número da lista é:", n1)

elif n2 >= n1 and n2 >= n3:
    print("O maior número da lista é:", n2)

else:
    print("O maior número da lista é:", n3)

    if n1 <= n2 and n1 <= n3:
        print("O menor número da lista é:", n1)

    elif n2 <= n1 and n2 <= n3:
        print("O menor número da lista é:", n2)

    else:
        print("O menor número da lista é:", n3)


