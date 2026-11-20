print("Vamos ler 5 idades e alturas e mostrar os dados na ordem inversa.")

idades = []
alturas = []

for i in range(5):
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))

    idades.append(idade)
    alturas.append(altura)

print("Idades na ordem inversa:", idades[::-1])
print("Alturas na ordem inversa:", alturas[::-1])