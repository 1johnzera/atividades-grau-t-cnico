tamanho_mb = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_mbps = float(input("Digite a velocidade da Internet em Mbps: "))

tamanho_megabits = tamanho_mb * 8
tempo_segundos = tamanho_megabits / velocidade_mbps
tempo_minutos = tempo_segundos / 60

print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos")