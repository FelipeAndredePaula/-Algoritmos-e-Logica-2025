print("Avaliador de Desempenho em Quiz\n============================".upper())
n_questoes = int(input("Digite a quantidade de questões do quiz (número inteiro positivo): "))
pontuacao_bruta = 0
erros_consecutivos = 0
for i in range(1,n_questoes+1):
    pontuacao = float(input(f"Digite a pontuação obtida na questão {i}: "))
    if pontuacao == 10:
        pontuacao_bruta += pontuacao
        erros_consecutivos = 0
    elif pontuacao < 5:
        pontuacao_bruta += pontuacao
        erros_consecutivos += 1
    else:
        pontuacao_bruta += pontuacao
        erros_consecutivos = 0
if pontuacao_bruta > 40 and erros_consecutivos == 0:
    print("Resultado Excelente! Bônus de 10% aplicado.")
    pontuacao_ajustada = pontuacao_bruta * 1.10
elif pontuacao_bruta < 20 or erros_consecutivos > 2:
    print("Resultado Fraco. Penalidade de 15% aplicada.")
    pontuacao_ajustada = pontuacao_bruta * 0.85
else:
    print("Resultado Padrão. Sem bônus ou penalidade.")
    pontuacao_ajustada = pontuacao_bruta
print(f"============================\nA pontuação bruta foi de: {pontuacao_bruta}\nA pontuação ajustada final foi de: {pontuacao_ajustada}")