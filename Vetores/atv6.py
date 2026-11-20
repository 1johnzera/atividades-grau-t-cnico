print("Vamos ler 4 notas de 10 alunos e calcular suas médias.")

medias = []
aprovados = 0

for i in range(10):
    soma = 0

    for j in range(4):
        nota = float(input("Digite uma nota: "))
        soma = soma + nota

    media = soma / 4
    medias.append(media)

    if media >= 7:
        aprovados = aprovados + 1

print("Médias dos alunos:", medias)
print("Quantidade de alunos aprovados:", aprovados)