print("Vamos mostrar a tabuada de um número digitado.")


numero = int(input("Digite um número de 1 a 10: "))

print("Tabuada de", numero, ":")

for i in range(1, 11):
    resultado = numero * i
    print(numero, "X", i, "=", resultado)
