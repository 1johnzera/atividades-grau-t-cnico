print("Vamos calcular a área do terreno.")

def area(largura, comprimento):
    resultado = largura * comprimento
    print("A área do terreno é:", resultado)

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))

area(largura, comprimento)