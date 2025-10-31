print("Calculadora de Temperatura Média\n\
====================================".upper())
n_dias = int(input("Digite a quantidade de dias\
 a serem analisados: "))
soma_temp = 0
print("Informe as temperaturas em graus Celsius")
for i in range(1,n_dias+1):
    temp = float(input(f"Digite a temperatura\
 registrada no {i}º dia: "))
    soma_temp += temp
media_temp = soma_temp / n_dias
print(f"====================================\
\nMédia da temperatura do período: {media_temp:.2f}")
if media_temp > 28:
    print("Média de temperatura: Clima Quente.")
elif media_temp >= 18 and media_temp <= 28:
    print("Média de temperatura: Clima Agradável.")
else:
    print("Média de temperatura: Clima Frio.")