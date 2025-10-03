#Felipe André Silva de Paula
#0220482523046
#EsteeO6Exercício
print("Felipe André Silva de Paula, RA 0220482523046")
#Entrada de dados
print("==================================")
print("AVALIADOR DE DESEMPENHO DE INVESTIMENTO")
retorno_investimento = float(input("Digite o valor decimal do retorno do investimento: "))
taxa_livre_risco = float(input("Digite o valor decimal da taxa livre de risco: "))
desvio_padrao = float(input("Digite o valor decimal do desvio padrão da volatilidade: "))
#Processamento de dados
if desvio_padrao == 0:
    input("O valor do desvio padrão precisa ser DIFERENTE de 0, informe um novo valor: ")
sharp = (retorno_investimento - taxa_livre_risco)/desvio_padrao
spread_risco = retorno_investimento - taxa_livre_risco
print("==================================")
#Término do processamento dos dados junto com a saída deles
if sharp > 1.5 and spread_risco > 0.05:
    print(f"Sharp Ratio: {sharp:.2f}\nCLASSIFICAÇÃO: Investimento Excelente: Alta performance ajustada ao risco.")
elif (sharp >= 0.5 and sharp <= 1.5) or spread_risco > 0.02:
    print(f"Sharp Ratio: {sharp:.2f}\nCLASSIFICAÇÃO: Investimento Bom: Risco e retorno moderados.")
elif sharp > 0.5 and retorno_investimento > 0:
    print(f"Sharp Ratio: {sharp:.2f}\nCLASSIFICAÇÃO: Investimento Aceitável: Retorno positivo, mas risco alto para o ganho.")
else:
    print(f"Sharp Ratio: {sharp:.2f}\nCLASSIFICAÇÃO: Investimento Ruim: Não recomendado.")