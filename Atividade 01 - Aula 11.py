print("Classificador de Múltiplos e Quadrados\n========================================".upper())

num = int(input("Digite o limite da contagem (número inteiro positivo): "))
soma_dos_quadrados = 0
for i in range(1,num+1):
    quadrado_num_atual = i**2
    if quadrado_num_atual % 3 == 0:
        print(f"{i} é múltiplo de 3.")
    elif quadrado_num_atual % 2 == 0:
        soma_dos_quadrados += quadrado_num_atual
        print(f"{i} é par. Quadrado acumulado.")
    else:
        print(f"{i} é ímpar, ignorado.")
print(f"========================================\nO valor final das somas dos quadrados dos números pares é de: {soma_dos_quadrados}.")

    