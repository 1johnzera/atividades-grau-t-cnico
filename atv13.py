gigabytes = float(input("Digite o tamanho do arquivo em GB: "))

megabytes = gigabytes * 1024
kilobytes = gigabytes * 1024 * 1024

print(f"Tamanho do arquivo em megabytes: {megabytes:.2f} MB")
print(f"Tamanho do arquivo em kilobytes: {kilobytes:.2f} KB")