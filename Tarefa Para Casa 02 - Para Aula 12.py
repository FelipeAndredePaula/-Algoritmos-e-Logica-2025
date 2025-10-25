print("Análise de Produtividade e Bônus\n================================".upper())
n_dias = int(input("Digite a quantidade de dias a serem analisados: "))
producao_total = 0
dias_acima_da_meta = 0
meta_diaria = 50
for i in range(1,n_dias+1):
    producao_dia = int(input(f"Digite a produção do {i}º dia: "))
    producao_total += producao_dia
    if producao_dia >= meta_diaria:
        dias_acima_da_meta += 1
media_diaria = producao_total / n_dias
if media_diaria > 60 and dias_acima_da_meta >= 4:
    print("BÔNUS MÁXIMO! (15% sobre a produção total)")
    bonus = producao_total * 0.15
elif media_diaria > 50 or dias_acima_da_meta >= 3:
    print("BÔNUS PARCIAL! (5% sobre a produção total)")
    bonus = producao_total * 0.05
else:
    print("Sem Bônus. Metas de produtividade não foram atingidas.")
    bonus = 0
print(f"================================\nMédia diária de produção: {media_diaria:.2f}\
      \nValor final do bônus: R${bonus:.2f}")