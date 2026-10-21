import math

area = float(input("Digite a área a ser pintada em m²: "))

litros_necessarios = area / 3
latas = math.ceil(litros_necessarios / 18)
preco_total = latas * 80

print(f"Litros de tinta necessários: {litros_necessarios:.2f} L")
print(f"Quantidade de latas a comprar: {latas}")
print(f"Preço total: R$ {preco_total:.2f}")