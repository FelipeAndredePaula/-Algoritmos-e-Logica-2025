print("Classificador de Desempenho de Vendedores com Bônus Condicional\n\
====================================".upper())
n_vendedores = int(input("Digite a quantidade de vendedores a serem analisa\
dos: "))
val_base_bonus = 500
pontuacao_total = 0
vendedores_ac_media = 0
vendedores_ab_media = 0
for i in range(1,n_vendedores+1):
    pontuacao_ind = int(input(f"Digite a pontuação final de vendas do {i}º\
 vendedor: "))
    pontuacao_total += pontuacao_ind
    if pontuacao_ind >= 90:
        vendedores_ac_media += 1
    elif pontuacao_ind < 50:
        vendedores_ab_media += 1
media_pontuacao_total = pontuacao_total / n_vendedores
val_base_bonus_total = val_base_bonus * n_vendedores
if media_pontuacao_total > 80 and vendedores_ab_media == 0:
    fmb = 1.2
elif vendedores_ac_media > (n_vendedores/2) or (media_pontuacao_total >= 70 and media_pontuacao_total <= 80):
    fmb = 1.05
elif vendedores_ab_media > 1:
    fmb = 0.8
else:
    fmb = 1
val_final_total = val_base_bonus_total*fmb
print(f"====================================\nMédia de pontuação da equipe\
: {media_pontuacao_total:.2f}\nNúmero de alertas: {vendedores_ab_media}\n\
Valor final total a pagar: R${val_final_total:.2f}")