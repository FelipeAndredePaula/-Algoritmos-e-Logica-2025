print("Calculadora de Temperatura Média")
qnt_dias = int(input("Digite a quantidade de dias a serem analisados: "))
soma_temperaturas = 0
for i in range(1, qnt_dias+1):
    graus = float(input(f"Digite a temperatura do {i}º dia: "))
    soma_temperaturas = soma_temperaturas + graus
media_temperaturas = soma_temperaturas/qnt_dias
print(f"===================================================\nMédia das temperaturas: {media_temperaturas:.2f}")
if media_temperaturas > 28:
    print("Clima Quente.")
elif media_temperaturas >= 18 and media_temperaturas <= 28:
    print("Clima Agradável.")
else:
    print("Clima Frio.")
