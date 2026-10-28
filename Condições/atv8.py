print("Quer saber qual produto comprar? simbora! ")

prod1 = float(input("Digite o preço do primeiro produto: "))
prod2 = float(input("Digite o preço do segundo produto: "))
prod3 = float(input("Digite o preço do terceiro produto: ")) 

if prod1 <= prod2 and prod1 <= prod3:
    print("O produto mais barato é o primeiro, que custa R$:",prod1)

elif prod2 <= prod1 and prod2 <= prod3:
    print("O produto mais barato é o segundo, que custa R$:",prod2)
else:
    print("O produto mais barato é o terceiro, que custa R$:",prod3)
    