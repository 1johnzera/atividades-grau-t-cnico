print("Vamos verificar qual número é maior.")

def maior(a, b):
    if a > b:
        print("O primeiro número é maior:", a)
    elif b > a:
        print("O segundo número é maior:", b)
    else:
        print("Os números são iguais!")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

maior(n1, n2)