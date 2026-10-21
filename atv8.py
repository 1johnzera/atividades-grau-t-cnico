print("Vamos calcular o seu salario?")

valor_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

salario = valor_hora * horas_trabalhadas

print(f"Seu salário total no mês é de: R$ {salario:.2f}")