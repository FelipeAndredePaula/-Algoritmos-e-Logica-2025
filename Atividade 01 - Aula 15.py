# Leitura da quantidade de elementos 
tamanho_vetor = int(input("Quantos números inteiros você deseja inserir no vetor? "))

vetor_numeros = [0] * tamanho_vetor
soma_pares = 0
print("\n--- Inserindo Elementos no Vetor ---")

for i in range(tamanho_vetor):
    # Lemos o número e atribuímos diretamente ao índice [i]
    numero = int(input(f"Digite o elemento {i + 1}º, (posição [{i}]): "))
    vetor_numeros[i] = numero

print(f"\nVetor principal criado: {vetor_numeros}")
print("--- Calculando Soma dos Pares ---")

for i in range(tamanho_vetor):
    elemento_atual = vetor_numeros[i]
    if elemento_atual % 2 == 0:
        soma_pares = soma_pares + elemento_atual
        print(f" Elemento par encontrado: {elemento_atual}")
    else:
        print(f"Elemento ímpar: {elemento_atual} (Ignorado)")

print("\n--- Resultado Final ---")
print(f"A soma de todos os elementos pares no vetor é: {soma_pares}")