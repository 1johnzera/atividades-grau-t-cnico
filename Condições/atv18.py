
print("Vamos descobrir se a data é válida! ")

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if mes in [1, 3, 5, 7, 8, 10, 12]:
    max_dias = 31
elif mes in [4, 6, 9, 11]:
    max_dias = 30
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        max_dias = 29
    else:
        max_dias = 28
else:
    max_dias = 0

if 1 <= dia <= max_dias:
    print("Tá certo, a data é válida!" )
else:
    print("Ta tentando enganar quem?" ) 
