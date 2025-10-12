print("Cálculo de Imposto e Taxas sobre Vendas")
qnt_dias = int(input("Digite a quantidade de dias: "))
vendas_totais = 0
for i in range(1, qnt_dias+1):
    valor_venda = float(input(f"Digite o valor de vendas do {i}º dia: "))
    vendas_totais = vendas_totais + valor_venda
media_vendas = vendas_totais/qnt_dias
if media_vendas > 1500:
    imposto_fixo = 200
else:
    imposto_fixo = 50
if vendas_totais <10000:
    pct_taxa_servico = 8
    taxa_servico = vendas_totais*0.08
else:
    pct_taxa_servico = 5
    taxa_servico = vendas_totais*0.05 
valor_final = vendas_totais - taxa_servico - imposto_fixo
print(f"============================\nValor total das vendas é de: R${vendas_totais}\nValor líquido final: R${valor_final}\nValor do imposto fixo aplicado: R${imposto_fixo}\nPercentual da taxa de serviço: {pct_taxa_servico}% = R${taxa_servico}")
