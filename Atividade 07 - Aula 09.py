qnt_prod_dif = int(input("Digite a quantidade de produtos diferentes que irá comprar: "))
total_de_compra = 0
for i in range(1, qnt_prod_dif+1):#como o range começará no segundo valor ajustamos a delimitador de fim para +1
    valor = float(input(f"Digite o valor do {i}º produto: "))
    total_de_compra = total_de_compra + valor
print(f"=======================================\nA soma dos valores dos {qnt_prod_dif} produtos é de {total_de_compra:.2f}")