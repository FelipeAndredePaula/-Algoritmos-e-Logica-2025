#Felipe André Silva de Paula
#0220482523046
#DESAFIO
#print("Felipe André Silva de Paula, RA 0220482523046")
#Entrada de dados
print("==================================")
print("CLASSIFICADOR DE LOTE QUÍMICO E PREÇO VARIÁVEL")
pureza_lote = float(input("Digite o valor decimal do percentual de pureza do lote: "))
massa_total = float(input("Digite o valor em KG da massa total: "))
taxa_contaminacao = float(input("Digite o valor decimal do percentual da taxa e contaminação: "))

#Processamento
fator_desempenho = (pureza_lote*100)-(taxa_contaminacao*50)
#Condicional para definir o valor da variável "massa_total"
if massa_total > 1000:
    preco_base_kg = 10
else:
    preco_base_kg = 12.50

#Estrutura condicional mestre contendo os últimos processamentos de dados e saída de deles
if fator_desempenho > 90 and pureza_lote > 0.98:
    print("Classificação: PREMIUM (Venda Imediata)")
    preco_total_kg = preco_base_kg*1.5 #aplica um bonus de 50%
    preco_total_lote = preco_total_kg*massa_total
    print(f"O preço base por KG é de R${preco_base_kg}\nO preço final por KG é de R${preco_total_kg}\nE o preço total do lote é de R${preco_total_lote}")

elif fator_desempenho > 70 and fator_desempenho < 90 and taxa_contaminacao <= 0.05:
    print("Classificação: PADRÃO (Venda Normal)")
    preco_total_kg = preco_base_kg*1.1 #aplica um bonus de 10%
    preco_total_lote = preco_total_kg*massa_total
    print(f"O preço base por KG é de R${preco_base_kg}\nO preço final por KG é de R${preco_total_kg}\nE o preço total do lote é de R${preco_total_lote}")

elif fator_desempenho < 70 or pureza_lote < 0.90:
    print("Classificação: REPROVADO (Descarte ou Re-processamento)")
    preco_total_kg = preco_base_kg*0.75 #aplica um desconto de 75%
    preco_total_lote = preco_total_kg*massa_total
    print(f"O preço base por KG é de R${preco_base_kg}\nO preço final por KG é de R${preco_total_kg}\nE o preço total do lote é de R${preco_total_lote}")

else:
    print("Classificação: ACEITÁVEL (Margem Mínima)")
    preco_total_kg = preco_base_kg*0.90 #aplica desconto de 90%
    preco_total_lote = preco_total_kg*massa_total
    print(f"O preço base por KG é de R${preco_base_kg}\nO preço final por KG é de R${preco_total_kg}\nE o preço total do lote é de R${preco_total_lote}")