#Parte 1: Simulação da Produção (Geração dos Dados)
print("Simulação de Produção e Venda com Dupla Análise\n\
====================================".upper())
n_lotes = int(input("Digite a quantidade de lotes de produção a serem\
 analisados: "))
c_fixo = 100
lista_c_por_lote = []
for i in range(1,n_lotes+1):
    un_prod = int(input(f"Digite a quantidade de unidades produzidas no\
 {i}º lote: "))
    if un_prod > 50:
        c_var_un = 1.5
    elif un_prod >= 20 and un_prod <= 50:
        c_var_un = 2
    else:
        c_var_un = 3
    c_total_lote = un_prod*c_var_un+c_fixo
    lista_c_por_lote.append(c_total_lote)
#Parte 2: Análise da Venda e Classificação (Processamento dos Dados Gerados)
p_base_venda_un = 5
lucro_total_ac = 0
lotes_lucro_alto = 0
print("====================================")
for index_lote, c_lote in enumerate(lista_c_por_lote,start=1):
    receita = 50*p_base_venda_un
    lucro = receita - c_lote
    if lucro > 100:
        lotes_lucro_alto += 1
        print(f"{index_lote}º lote: Aprovado: lucro alto.")
    elif lucro > 0:
        print(f"{index_lote}º lote: Aceitável: lucro mínimo.")
    else:
        print(f"{index_lote}º lote: Reprovado: prejuízo.")
    lucro_total_ac += lucro
print(f"Lucro total acumulado: R${lucro_total_ac:.2f}\nQuantidade de lotes\
 com lucro alto: {lotes_lucro_alto}")