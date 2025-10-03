#Felipe André Silva de Paula
#0220482523046
#01Marcus
#print("Felipe André Silva de Paula, RA 0220482523046")
#Entrada de dados
print("==================================")
print("CLASSIFICADOR DE LUCRO DE VENDAS")
preco_custo = float(input("Digite o preço de custo do produto: "))
preco_venda = float(input("Digite o preço de venda do produto: "))
print("==================================")
#Processamento dos dados inseridos
lucro = preco_venda-preco_custo
margem_lucro = (lucro/preco_custo)*100
#Início do bloco condicional para saída com mensagem apropriada
if margem_lucro > 30:
    print("Margem Excelente!")
elif margem_lucro >= 10 and margem_lucro <= 30:
    print("Margem Satisfatória.")
else:
    print("Margem Baixa: Avaliar preço de venda.")