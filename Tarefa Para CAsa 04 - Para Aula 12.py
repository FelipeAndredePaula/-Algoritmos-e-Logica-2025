print("Avaliador de Lançamentos Financeiros\n================================".upper())
n_lancamentos = int(input("Informe a quantidade de lançamentos a serem\
analisados: "))
saldo_final = 0
total_receitas = 0
total_despesas = 0
for i in range(1, n_lancamentos+1):
    valor_tran = float(input(f"Digite o valor do {i}º lançamento: "))
    if valor_tran > 0:
        total_receitas += valor_tran
    else:
        total_despesas += valor_tran
    saldo_final += valor_tran
if saldo_final > 0 and total_receitas > 2*total_despesas:
    print("Situação Excelente: Bônus de 5% sobre o saldo aplicado.")
    saldo_ajustado = saldo_final*1.05
elif saldo_final > 0:
    print("Situação Regular: Sem bônus ou taxa.")
    saldo_ajustado = saldo_final
else:
    print("Situação Ruim: Taxa de serviço de 2% aplicada.")
    saldo_ajustado = saldo_final * 0.98
print(f"================================\nTotal de receitas: R${total_receitas:.2f}\
      \nTotal de despesas: R${total_despesas*-1:.2f}\nSaldo final ajustados\
: R${saldo_ajustado:.2f}")