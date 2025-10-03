#Felipe André Silva de Paula
#0220482523046
#AmOmatta
#print("Felipe André Silva de Paula, RA 0220482523046")
#Entrada de dados
print("==================================")
print("CALCULADORA DE INVESTIMENTO COM RENTABILIDADE CONDICIONAL")
valor_inicial = float(input("Digite o valor inicial do investimento: "))
prazo = int(input("Digite o prazo do investimento em meses inteiros: "))
print("==================================")
#Processamento de dados com estrutura condicional
if prazo < 6:
    taxa_juros = 0.005
    valor_final = valor_inicial*taxa_juros*prazo
    #Saída de dados
    print(f"A taxa de juros mensal aplicada para o investimento em questão é de 0.5% ao mês\nO rendimento total obtido será de R${valor_final}")
elif prazo >= 6 and prazo <= 12:
    taxa_juros = 0.008
    valor_final = valor_inicial*taxa_juros*prazo
    #Saída de dados
    print(f"A taxa de juros mensal aplicada para o investimento em questão é de 0.8% ao mês\nO rendimento total obtido será de R${valor_final}")
else:
    taxa_juros = 0.012
    valor_final = valor_inicial*taxa_juros*prazo
    #Saída de dados
    print(f"A taxa de juros mensal aplicada para o investimento em questão é de 1.2% ao mês\nO rendimento total obtido será de R${valor_final}")
