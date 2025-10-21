print("Análise de Produtividade com Penalidade Condicional\n====================================".upper())
sal_base_mensal = 800
lim_falhas_sem = 1
cont_falhas = 0
prod_semanal = 0
print("A escala da produtividade diária é de 0-100 (número inteiro)")
for i in range(5):
    if i == 0:
        prod_diaria = int(input("Digite a produtivadade do funcionário na segunda-feira: "))
    elif i == 1:
        prod_diaria = int(input("Digite a produtivadade do funcionário na terça-feira: "))
    elif i == 2:
        prod_diaria = int(input("Digite a produtivadade do funcionário na quarta-feira: "))
    elif i == 3:
        prod_diaria = int(input("Digite a produtivadade do funcionário na quinta-feira: "))
    else:
        prod_diaria = int(input("Digite a produtivadade do funcionário na sexta-feira: "))
    prod_semanal += prod_diaria
    if prod_diaria < 60:
        cont_falhas += 1 
media_prod = prod_semanal / 5
print("====================================")
if media_prod > 80 and cont_falhas <= lim_falhas_sem:
    print("Pagamento Máximo: Bônus de 10% aplicado.")
    sal_total_mensal = sal_base_mensal*1.1
elif media_prod >= 60 and media_prod <= 80 or cont_falhas > lim_falhas_sem:
    print("Pagamento Padrão: Penalidade de 5% aplicada (Devido a falhas).")
    sal_total_mensal = sal_base_mensal *0.95
else:
    print("Penalidade Severa: Pagamento reduzido em 25%.")
    sal_total_mensal = sal_base_mensal*0.75
print(f"Produtividade média: {media_prod:.2f}\nContagem de falhas: {cont_falhas}\nPagamento final do funcionário: R${sal_total_mensal:.2f}")