#Felipe André Silva de Paula
#0220482523046
#VaiSaoPaulo
#print("Felipe André Silva de Paula, RA 0220482523046")
#Entrada de dados
print("==================================")
print("CALCULADORA DE CUSTO DE ENVIO COM TAXAS VARIÁVEIS")
peso_encomenda = float(input("Digite o peso da encomenda em KG: "))
distancia_entrega = float(input("Digite a distância da entrega em KM: "))
print("==================================")
#Processamento de dados
custo_base = (peso_encomenda*1.5)+(distancia_entrega*0.25)
#Bloco condicional para calcular o valor apropriado e apresentar a saída dos dados
if custo_base > 200:
    custo_final = custo_base-(custo_base*0.1)
    print(f"O custo base original do produto é de R${custo_base}\nO custo final do produto é de R${custo_final}. Desconto de 10% aplicado!")
elif custo_base >= 50 and custo_base <=200:
    custo_final = custo_base
    print(f"O custo base original do produto é de R${custo_base}\nO custo final do produto também é de R${custo_final}. Nenhum desconto disponível para esta faixa de preço")
else:
    custo_final = custo_base + 5
    print(f"O custo base original do produto é de R${custo_base}\nO custo final do produto é de R${custo_final}. Taxa de R$5.00 aplicada para cobrir os custos de frete.")
