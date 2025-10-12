qnt_notaf = int(input("Digite a quantidade de notas fiscais: "))
soma_notaf = 0
for i in range(1, qnt_notaf+1):
    valor = float(input(f"Digite o valor da {i}ª nota fiscal: "))
    soma_notaf = soma_notaf + valor

if soma_notaf >= 15000:
    aliquota = 0.16
elif soma_notaf >= 5000 and soma_notaf < 15000:
    aliquota = 0.12
elif soma_notaf >= 1000 and soma_notaf < 5000:
    aliquota = 0.09
else:
    aliquota = 0.05
valor_imposto = soma_notaf*aliquota
aliquota_pct = aliquota*100
print(f"===================================\nAlíquota aplicada: {aliquota_pct}%\nValor total das notas: R${soma_notaf}\nValor total de impostos: R${valor_imposto}")