
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

op = input("Escolha a operação (+, -, *, /): ")

if op == "+":
    resultado = n1 + n2
elif op == "-":
    resultado = n1 - n2
elif op == "*":
    resultado = n1 * n2
elif op == "/" and n2 != 0:
    resultado = n1 / n2
else:
    resultado = None
    print("Operação inválida!")

if resultado is not None:
    print("Resultado:", resultado)

    if resultado > 0:
        print("Positivo")
    elif resultado < 0:
        print("Negativo")
    else:
        print("Zero")

    if resultado == int(resultado):
        print("Inteiro")
    else:
        print("Decimal")

    if resultado == int(resultado):
        if int(resultado) % 2 == 0:
            print("Par")
        else:
            print("Ímpar")
    else:
        print("Dá não fih! nem é um número inteiro, como é que quer saber se é par ou ímpar?")
