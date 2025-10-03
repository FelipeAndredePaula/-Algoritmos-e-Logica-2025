#Felipe André Silva de Paula
#0220482523046
#AmorFino
#print("Felipe André Silva de Paula, RA 0220482523046")
#Entrada de dados
print("==================================")
print("CALCULADORA DE CUSTO FINAL DE PRODUÇÃO COM PENALIDADE")
custo_inicial_C = float(input("Digite o custo inicial do material: "))
quantidade_produzida_Q = int(input("Digite a quantidade produzida do material: "))
#Condicional para verificar se houve atraso
atraso = input("Houve dias de atraso na produção (digite apenas 'sim' ou 'não'): ")
if atraso == "sim":
    dias_atraso = int(input("Digite a quantidade de dias de atraso: "))
else:
    dias_atraso = 0
#Recebe o valor em porcentagem e converte para seu equivalente decimal
percentual_defeito = float(input("Digite o PERCENTUAL de defeitos da produção em questão (ex. 5, 10): "))
percentual_defeito = percentual_defeito / 100
#Processamento de dados
if quantidade_produzida_Q > 1000 and custo_inicial_C > 5000:
    fator_complexidade = 1.15
else:
    fator_complexidade = 1.0

custo_base_corrigido = custo_inicial_C*fator_complexidade
print("==================================")
#Processamento da última variável "custo_final" junto com a saída de dados em um bloco condicional
if percentual_defeito > 0.1 or dias_atraso > 0:
        print("Penalidade Alta: 25% de redução no lucro.")
        custo_final = custo_base_corrigido*0.75
        print(f"O custo base corrigido do lote é de R${custo_base_corrigido}\nE o custo final do lote é de R${custo_final}")
elif percentual_defeito > 0.05 and percentual_defeito <= 0.1 and dias_atraso > 0:
        print("Penalidade Média: 10% de redução no lucro.")
        custo_final = custo_base_corrigido*0.90
        print(f"O custo base corrigido do lote é de R${custo_base_corrigido}\nE o custo final do lote é de R${custo_final}")
else:
    print("Sem penalidade. Custo final apenas com correção.")
    custo_final = custo_base_corrigido
    print(f"O custo final do lote é o mesmo do custo base corrigido que é de R${custo_final}")