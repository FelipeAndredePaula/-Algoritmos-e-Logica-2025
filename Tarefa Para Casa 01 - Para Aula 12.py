print("Análise de Bônus de Vendas e Desempenho\n================================".upper())
V_base = float(input("Digite o valor base do bônus: "))
P_ind = int(input("Digite a pontuação de performance individual (0-100): "))
P_equipe = int(input("Digite a pontuação de meta da equipe (0-100): "))
if P_ind > 90:
    FAP = 1.25
elif P_ind > 70:
    FAP = 1.1
elif P_ind > 50:
    FAP = 0.8
B_ajustado = V_base*FAP
if P_equipe > 85:#meta de equipe alta
    if P_ind > 95 or B_ajustado > 5000:
        print("Bônus Máximo (30% Extra)")
        B_final = B_ajustado * 1.3
    else:#meta alta mas desempenho individual mediano
        print("Bônus Padrão (10% Extra")
        B_final = B_ajustado * 1.1
elif P_equipe >= 60 and P_equipe <= 85:#meta de equipe média
    if P_ind < 60:
        print("Penalidade por Desempenho Individual (15% de Redução)")
        B_final = B_ajustado * 0.85
    else:#desempenho individual aceitável
        print("Sem Alteração Adicional.")
        B_final = B_ajustado
else:#meta de equipe baixa
    print("Penalidade Severa (25% de Redução)")
    B_final = B_ajustado * 0.75
print(f"================================\nValor base bônus: R${V_base}\
      \nFator de ajuste aplicado: {FAP}\nBônus final: R${B_final:.2f}")
    