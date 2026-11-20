print("Vamos ler 4 notas.")

notas = []

for i in range(4):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

media = sum(notas) / 4

print("Notas:", notas)
print("Média:", media)