print("O CUSTO DE PRODUÇÃO DE UM LOTE DE 100 ITENS\n=================================")
custo_total_producao = 0
custo_fixo_lote = 500
custo_mat_prima = float(input("Digite o valor da matéria-prima por item: "))
desperdicio = custo_mat_prima*0.05
custo_var_lote = custo_mat_prima+desperdicio
for i in range(100):
    custo_total_producao += custo_var_lote
custo_total_producao += custo_fixo_lote
if custo_total_producao < 3000:
    margem_lucroM = 0.35
elif custo_total_producao >= 3000 and custo_total_producao <= 5000:
    margem_lucroM = 0.2
else:
    margem_lucroM = 0.15
preco_minimo = (custo_total_producao/100)*(1+margem_lucroM)
print(f"=================================\nCusto total de produção: R${custo_total_producao:.2f}\nMargem de lucro aplicada: {margem_lucroM*100}%\nPreço mínimo de venda por item: R${preco_minimo:.2f}")