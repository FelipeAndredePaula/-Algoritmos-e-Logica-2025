print("Avaliador de Retorno de Investimento Mensal\n==========================".upper())
v_inicial = float(input("Digite o valor inicial do investimento: "))
n_meses = int(input("Digite a quantidade de meses inteiros a serem simulados: "))
v_acumulado = v_inicial
juros_totais = 0
for i in range(1,n_meses+1):
    taxa_cres_mensal = float(input(f"Digite a taxa de crescimento do {i}º mês em decimal (ex: 0.02 para 2%): "))
    if taxa_cres_mensal > 0.015:
        juros = v_acumulado*taxa_cres_mensal
    elif taxa_cres_mensal >= 0.005 and taxa_cres_mensal <= 0.015:
        juros = v_acumulado*taxa_cres_mensal*0.9
    else:
        juros = 0
    v_acumulado += juros
    juros_totais += juros
print(f"==========================\nValor acumulado: R${v_acumulado:.2f}\nJuros totais: R${juros_totais:.2f}")
if juros_totais > (v_inicial*0.1):
    print("Investimento de Alto Sucesso! (Retorno superior a 10%)")
else:
    print("Investimento Moderado. Retorno abaixo do esperado.")

