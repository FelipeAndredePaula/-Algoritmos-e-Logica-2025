qnt_dias = int(input("Digite a quantidade de dias da viagem: "))
total_km_percorridos = 0
for i in range(1, qnt_dias+1):
    km_dia = float(input(f"Digite a quantidade (em KM) percorrida no {i}º dia: "))
    total_km_percorridos = total_km_percorridos + km_dia
    total_litros_carro = total_km_percorridos / 12
    custo_comb_carro = total_litros_carro*4.80
print(f"=========================\nTotal de KM percorridos: {total_km_percorridos:.2f}\nCusto total to percurso: {custo_comb_carro:.2f}")
if custo_comb_carro > 500:
    print("Alerta de Gastos: O custo total com combustível foi alto (Acima de R$ 500,00).")
else:
    print("Gastos sob controle: O custo total com combustível foi baixo ou moderado.")
