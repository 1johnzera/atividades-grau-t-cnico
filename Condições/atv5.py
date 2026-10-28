print("Vamos calcular a sua nota? ")

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Você foi aprovado pra krl, parabéns! ")

elif media >= 7:
    print("Passou hein? ai sim! ")

elif media < 7:
    print("Vish.. deu não parceiro, tenta na próxima! ")
