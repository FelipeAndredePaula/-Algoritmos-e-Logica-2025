print("Cálculo de Imposto sobre Notas Fiscais\n==============================".upper())
qnt_ntficais = int(input("Digite a quantidade de notas ficais a serem inseridas: "))
soma_das_notas = 0
for i in range(1,qnt_ntficais+1):
    nota = float(input(f"Digite o valor da {i}ª nota fiscal: "))
    soma_das_notas += nota
if soma_das_notas > 15000:
    aliquota = 0.16
elif soma_das_notas >= 5000 and soma_das_notas <= 15000:
    aliquota = 0.12
elif soma_das_notas >= 1000 and soma_das_notas < 5000:
    aliquota = 0.09
else:
    aliquota = 0.05
valor_total_imposto = soma_das_notas*aliquota
print(f"==============================\nValor total das notas = R${soma_das_notas:.2f}\nAlíquota aplicada: {aliquota*100}%\nValor total do imposto: R${valor_total_imposto:.2f}")