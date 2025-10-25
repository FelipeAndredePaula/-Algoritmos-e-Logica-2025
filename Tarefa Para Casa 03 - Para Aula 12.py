print("Avaliação de Estoque com Fator de Risco\n================================".upper())
n_prod = int(input("Digite quantos produtos serão analisados: "))
valor_total_estoque = 0
prods_alto_risco = 0
for i in range(1,n_prod+1):
    preco_unidade = float(input(f"Digite o preço unitário do {i}º produto: "))
    qnt_em_estoque = int(input(f"Digite a quantidade em estoque do {i}º produto: "))
    valor_bruto_prod = preco_unidade*qnt_em_estoque
    if qnt_em_estoque > 100:
        valor_total_estoque += valor_bruto_prod*1.05
    elif (preco_unidade > 50) and (qnt_em_estoque <= 10):
        prods_alto_risco = prods_alto_risco + 1
        valor_total_estoque += valor_bruto_prod
    else:
        valor_total_estoque += valor_bruto_prod
print(f"================================\nValor total final do estoque\
: R${valor_total_estoque:.2f}\nNúmero de produtos classificados como alto\
 risco: {prods_alto_risco}")