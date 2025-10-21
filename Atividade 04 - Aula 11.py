print("Análise de Contas de Energia Elétrica\n==========================".upper())
n_meses = int(input("Digite a quantidade de meses inteiros a serem simulados: "))
consumo_total_kwh = 0
valor_total_pago = 0
for i in range(1, n_meses+1):
    consumo_kwh = float(input(f"Digite o consumo em kWh do {i}º mês: "))
    if consumo_kwh > 200:
        tarifa_por_kwh = 0.95
    elif consumo_kwh > 100 and consumo_kwh <= 200:
        tarifa_por_kwh = 0.70
    else:
        tarifa_por_kwh = 0.55
    custo_mensal = consumo_kwh*tarifa_por_kwh
    consumo_total_kwh +=consumo_kwh
    valor_total_pago += custo_mensal
print(f"==========================\nConsumo total em kWh: {consumo_total_kwh:.2f}\nValor total pago: R${valor_total_pago:.2f}")
media_mensal_consumo = consumo_total_kwh / n_meses
if media_mensal_consumo > 180:
    print("Alerta! O consumo médio está elevado. Sugerir medidas de economia.")
else:
    print("Consumo médio dentro dos limites normais.")
