print("Verificação de gênero.")

letra = input("Digite F ou M: ")

if letra in "Ff":
    print("O sexo designado foi: Feminino! ")

elif letra in "Mm":
    print("O sexo designado foi: Masculino! ")

else:
    print("Sexo Inválido! ")