print("Análise de Lote de Peças com Classificação de Erros\n\
====================================".upper())
n_pecas = int(input("Digite a quantidade de peças\
 a serem analisadas: "))
cust_fixo_insp_lote = 150
cust_retrabalho = 25
erros_crit = 0
erros_leve = 0
cust_var_rej = 0
for i in range (1,n_pecas+1):
    ni_def = int(input(f"Digite o nível de defeito da\
 {i}ª peça: "))
    if ni_def > 8:
        erros_crit += 1
        cust_var_rej += cust_retrabalho
    elif ni_def >= 3 and ni_def <= 8:
        erros_leve += 1
    else:
        print("Peça Aprovada.")
taxa_rej = (erros_crit/n_pecas)*100
cust_final = cust_fixo_insp_lote + cust_var_rej
print("====================================")
print(f"Taxa de rejeição: {taxa_rej:.2f}%\nCusto final\
 total: R${cust_final:.2f}")
if taxa_rej > 10 and erros_leve > 5:
    print("LOTE REPROVADO! Alta taxa de defeito e muitos erros leves.")
elif erros_crit > 2 or taxa_rej > 20:
    print("LOTE CRÍTICO! Necessário reavaliação total.")
else:
    print("LOTE APROVADO! Custos sob controle.")