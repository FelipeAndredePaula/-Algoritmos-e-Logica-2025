print(f"SOMADORA DE CINCO VALORES\n===================================")
soma = 0
for i in range(1, 6):
    num = int(input(f"Digite o {i}° valor a ser somado (número inteiro): "))
    soma = soma+num
print(f"===================================)\nA soma dos cinco valores informados é de: {soma}")
