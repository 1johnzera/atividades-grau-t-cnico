while True:
    nota = float(input("insira uma nota entre 0 e 10: "))

    if nota < 0 or nota > 10:
        print("Nota invalida, insira outra nota")

    else:
        break 